// Background starfield + era-tinted nebula for the timeline.
// Drawn on #bg, behind the main canvas. Toggle saved as tl-fx.
(function(){
var canvas=document.getElementById('bg');
if(!canvas)return;
var ctx=canvas.getContext('2d');
var W=0,H=0,uMin=-0.02,uMax=10.4,dpr=1;
var fxOn=true,reduced=false,hidden=false,running=false,raf=0;
var STARS=[],STAR_N=320;

try{var sv=localStorage.getItem('tl-fx');if(sv==='0')fxOn=false;}catch(_){}
function mq(){return window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;}
reduced=mq();

function rng(seed){var a=seed|0;return function(){a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function makeStars(){
  var r=rng(0x5F1E1),i,s;
  STARS=[];
  for(i=0;i<STAR_N;i++){
    s={
      x:r(),y:r(),
      z:0.18+r()*0.82,
      r:0.35+r()*1.35,
      b:0.25+r()*0.75,
      phase:r()*Math.PI*2,
      spd:0.0004+r()*0.0016,
      tint:r()<0.15?1:r()<0.3?2:0,
      halo:r()<0.08
    };
    if(r()<0.25)s.r*=0.6;
    STARS.push(s);
  }
}
makeStars();

// Era colour stops by log-years-ago (u). Cosmic violet → Earth amber → life green →
// prehistory/ancient gold → modern cool blue.
var STOPS=[
  {u:10.40,c:[78,40,150]},
  {u:9.95,c:[38,52,155]},
  {u:9.66,c:[175,78,32]},
  {u:9.20,c:[26,128,78]},
  {u:7.80,c:[60,112,58]},
  {u:5.20,c:[148,114,40]},
  {u:3.40,c:[158,120,52]},
  {u:2.20,c:[52,82,128]},
  {u:0.00,c:[30,50,98]}
];
function lerp(a,b,t){return a+(b-a)*t;}
function colorAt(u){
  var i,a,b,t;
  if(u>=STOPS[0].u)return STOPS[0].c.slice();
  for(i=0;i<STOPS.length-1;i++){
    if(u<=STOPS[i].u&&u>=STOPS[i+1].u){
      a=STOPS[i].c;b=STOPS[i+1].c;
      t=(STOPS[i].u-u)/Math.max(STOPS[i].u-STOPS[i+1].u,1e-6);
      return[lerp(a[0],b[0],t),lerp(a[1],b[1],t),lerp(a[2],b[2],t)];
    }
  }
  return STOPS[STOPS.length-1].c.slice();
}
function colorForView(){
  var n=5,acc=[0,0,0],i,c,u;
  for(i=0;i<n;i++){
    u=uMin+(uMax-uMin)*(i/(n-1));
    c=colorAt(u);
    acc[0]+=c[0];acc[1]+=c[1];acc[2]+=c[2];
  }
  return[acc[0]/n,acc[1]/n,acc[2]/n];
}

function resize(){
  var parent=canvas.parentNode;if(!parent)return;
  var r=parent.getBoundingClientRect();
  dpr=window.devicePixelRatio||1;
  W=r.width;H=r.height;
  canvas.style.width=W+'px';canvas.style.height=H+'px';
  canvas.width=Math.round(W*dpr);canvas.height=Math.round(H*dpr);
  ctx.setTransform(dpr,0,0,dpr,0,0);
  paint(performance.now());
}

function starXY(s){
  // Screen-space field with wrap; parallax from view centre and zoom, unless reduced motion.
  var x=s.x*(W+160)-80,y=s.y*H;
  if(!reduced){
    var cam=(uMin+uMax)/2,span=Math.max(uMax-uMin,0.001);
    var pan=(cam-5.2)*s.z*28;
    var zoom=Math.log(10.42/span)*s.z*14;
    x+=pan+zoom*(s.x-0.5)*8;
    y+=(cam-5.2)*s.z*4;
  }
  var tw=W+160;
  x=((x+80)%tw+tw)%tw-80;
  return[x,y];
}

function paint(now){
  ctx.setTransform(dpr,0,0,dpr,0,0);
  ctx.clearRect(0,0,W,H);
  if(!fxOn||W<2||H<2)return;

  var col=colorForView();
  var cam=(uMin+uMax)/2;
  var shift=reduced?0:(cam-5.2)*10;
  var gx=W*0.42-shift,gy=H*0.30;
  var R=Math.max(W,H)*0.62;
  var g=ctx.createRadialGradient(gx,gy,0,gx,gy,R);
  g.addColorStop(0,'rgba('+((col[0])|0)+','+((col[1])|0)+','+((col[2])|0)+',0.20)');
  g.addColorStop(0.45,'rgba('+((col[0])|0)+','+((col[1])|0)+','+((col[2])|0)+',0.07)');
  g.addColorStop(1,'rgba('+((col[0])|0)+','+((col[1])|0)+','+((col[2])|0)+',0)');
  ctx.fillStyle=g;ctx.fillRect(0,0,W,H);

  var c2=colorAt(uMin*0.35+uMax*0.65);
  var gx2=W*0.68+shift*0.5,gy2=H*0.72,R2=Math.max(W,H)*0.48;
  var g2=ctx.createRadialGradient(gx2,gy2,0,gx2,gy2,R2);
  g2.addColorStop(0,'rgba('+((c2[0])|0)+','+((c2[1])|0)+','+((c2[2])|0)+',0.10)');
  g2.addColorStop(1,'rgba('+((c2[0])|0)+','+((c2[1])|0)+','+((c2[2])|0)+',0)');
  ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);

  var mid=Math.round(H/2),i,s,p,x,y,tw,a,fade,rgb;
  for(i=0;i<STAR_N;i++){
    s=STARS[i];p=starXY(s);x=p[0];y=p[1];
    if(x<-4||x>W+4||y<-4||y>H+4)continue;
    fade=Math.abs(y-mid);
    fade=fade<30?0.12+0.88*(fade/30):1; // keep the timeline line clear
    // also ease off the top-left filters / bottom-left legend a little
    if(x<130&&y<56)fade*=0.35;
    if(x<170&&y>H-120)fade*=0.45;
    tw=(!reduced&&fxOn)?0.70+0.30*Math.sin(now*s.spd+s.phase):0.88;
    a=s.b*tw*fade*0.90;
    if(a<0.03)continue;
    if(s.tint===1)rgb='200,220,255';
    else if(s.tint===2)rgb='255,236,210';
    else rgb='255,255,255';
    if(s.halo){
      ctx.fillStyle='rgba('+rgb+','+(a*0.16)+')';
      ctx.beginPath();ctx.arc(x,y,s.r*3.2,0,6.283);ctx.fill();
    }
    ctx.fillStyle='rgba('+rgb+','+a+')';
    if(s.r<0.7){ctx.fillRect(Math.round(x),Math.round(y),1,1);}
    else{ctx.beginPath();ctx.arc(x,y,s.r,0,6.283);ctx.fill();}
  }
}

function loop(t){
  raf=0;
  if(!running)return;
  paint(t);
  raf=requestAnimationFrame(loop);
}
function start(){
  stop();
  if(!fxOn||hidden){paint(0);return;}
  if(reduced){paint(0);return;}
  running=true;
  raf=requestAnimationFrame(loop);
}
function stop(){
  running=false;
  if(raf){cancelAnimationFrame(raf);raf=0;}
}

function setView(a,b){
  if(a!=null){uMin=a;uMax=b;}
  paint(performance.now());
}

function syncBtn(){
  var b=document.getElementById('fxbtn');if(!b)return;
  b.setAttribute('aria-pressed',fxOn?'true':'false');
  b.title=fxOn?'Turn background effects off':'Turn background effects on';
  b.classList.toggle('off',!fxOn);
  b.innerHTML=fxOn?'&#10022; Effects':'&#10022; Effects off';
}
function setFx(on){
  fxOn=!!on;
  try{localStorage.setItem('tl-fx',fxOn?'1':'0');}catch(_){}
  syncBtn();
  if(fxOn)start();else{stop();paint(0);}
}

var btn=document.getElementById('fxbtn');
if(btn){
  btn.addEventListener('click',function(ev){ev.preventDefault();ev.stopPropagation();setFx(!fxOn);});
  syncBtn();
}

if(window.matchMedia){
  var mm=window.matchMedia('(prefers-reduced-motion: reduce)');
  var onMM=function(){reduced=mq();if(reduced)stop();start();};
  if(mm.addEventListener)mm.addEventListener('change',onMM);
  else if(mm.addListener)mm.addListener(onMM);
}
document.addEventListener('visibilitychange',function(){
  hidden=document.hidden;
  if(hidden)stop();else start();
});
window.addEventListener('resize',resize);

window.TLBG={setView:setView,resize:resize,setFx:setFx};
resize();
start();
})();
