(function(){
var D=window.TIMELINE_DATA, c=document.getElementById('c'), x=c.getContext('2d'), side=document.getElementById('side'),content=document.getElementById('content');
document.getElementById('close').onclick=function(){side.classList.remove('open');};
var NOW=2026, toU=function(y){return Math.log10(Math.max(NOW-y,1))}; // u: log10 years ago (0..~10.14)
var uMin=0, uMax=10.3, hits=[];
function resize(){c.width=c.parentNode.clientWidth;c.height=c.parentNode.clientHeight;draw();}
function px(u){return c.width-(u-uMin)/(uMax-uMin)*c.width;} // past on left
function fmt(ya){return ya>=1e9?(ya/1e9).toFixed(1)+' Bya':ya>=1e6?(ya/1e6).toFixed(1)+' Mya':ya>=1e4?Math.round(ya/1e3)+' kya':(NOW-ya<0?Math.round(ya-NOW)+' BCE':Math.round(NOW-ya)+' CE');}
function lbl(ya){var y=NOW-ya;if(ya>=1e9)return+(ya/1e9).toPrecision(3)+' Bya';if(ya>=1e6)return+(ya/1e6).toPrecision(3)+' Mya';if(ya>=1e5)return+(ya/1e3).toPrecision(4)+' kya';return y<=0?(1-y)+' BCE':y+' CE';}
function ticks(){var a=Math.pow(10,Math.max(uMin,0)),b=Math.pow(10,uMax),out=[];
 for(var p=Math.floor(Math.log10(Math.max((b-a)/12,1)));p<=Math.ceil(uMax);p++){var s=Math.pow(10,p);if(s<1)continue;
  if((b-a)/s<=60){for(var v=Math.ceil(a/s)*s;v<=b;v+=s)out.push({v:v,p:p});}
  else for(var k=1;k<10;k++){var v2=k*s;if(v2>=a&&v2<=b)out.push({v:v2,p:p,k:k});}}
 out.sort(function(m,n){return n.p-m.p||(m.k||1)-(n.k||1);});return out;}
function draw(){x.clearRect(0,0,c.width,c.height);var H=c.height,L=Math.round(H/2);hits=[];
 x.strokeStyle='#fff';x.lineWidth=2;x.beginPath();x.moveTo(0,L);x.lineTo(c.width,L);x.stroke();x.lineWidth=1;
 x.font='11px sans-serif';x.textAlign='center';var used=[];
 ticks().forEach(function(t){var p=px(Math.log10(t.v));if(p<0||p>c.width)return;var w=x.measureText(lbl(t.v)).width+14;
  for(var i=0;i<used.length;i++)if(Math.abs(used[i][0]-p)<(used[i][1]+w)/2)return;used.push([p,w]);
  x.strokeStyle='#bbb';x.beginPath();x.moveTo(p,L-8);x.lineTo(p,L);x.stroke();x.fillStyle='#ddd';x.fillText(lbl(t.v),p,L-12);});
 x.textAlign='left';var rows=[];
 D.entries.slice().sort(function(m,n){return m.start-n.start;}).forEach(function(e){var a=px(toU(e.start)),b=e.end!=null?px(toU(e.end)):a;
  var col=e.lane==='myth'?'#c9f':'#6cf';x.fillStyle=col;
  if(b-a>2){x.globalAlpha=.5;x.fillRect(a,L-3,b-a,6);x.globalAlpha=1;}
  if(e.lane==='myth'){x.beginPath();x.moveTo(a,L-7);x.lineTo(a+7,L);x.lineTo(a,L+7);x.lineTo(a-7,L);x.fill();}else{x.beginPath();x.arc(a,L,6,0,7);x.fill();}
  x.font='12px sans-serif';var w=x.measureText(e.title).width,r=0;while(rows[r]!=null&&rows[r]>a-4)r++;rows[r]=a+w+12;var y=L+26+r*18;
  x.strokeStyle='#555';x.beginPath();x.moveTo(a,L+7);x.lineTo(a,y-10);x.stroke();x.fillStyle='#eee';x.fillText(e.title,a+3,y);
  hits.push({e:e,x0:a-8,x1:a+w+6,y0:L-8,y1:y+4});});
 x.font='12px sans-serif';x.fillStyle='#6cf';x.beginPath();x.arc(14,H-30,5,0,7);x.fill();x.fillStyle='#eee';x.fillText('History / science',24,H-26);
 x.fillStyle='#c9f';x.beginPath();x.moveTo(14,H-20);x.lineTo(19,H-14);x.lineTo(14,H-8);x.lineTo(9,H-14);x.fill();x.fillStyle='#eee';x.fillText('Myth / legend',24,H-10);}
function esc(s){return String(s).replace(/[&<>"]/g,function(ch){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch];});}
function show(e){var h='<h3>'+esc(e.title)+'</h3><div>'+e.evidenceTypes.map(function(t){return'<span class="tag">'+esc(t)+'</span>';}).join('')+'</div>';
 h+='<p><b>Date:</b> '+(e.start<0?-e.start+' BCE':e.start+' CE')+(e.end!=null?' – '+(e.end<0?-e.end+' BCE':e.end+' CE'):'')+(e.dateNote?' <i>('+esc(e.dateNote)+')</i>':'')+'</p>';
 h+='<div class="cols"><div><b>Mainstream view</b><p>'+esc(e.mainstream)+'</p></div><div><b>Alternative views</b>'+(e.alternatives.length?e.alternatives.map(function(a){return'<p><i>'+esc(a.label)+':</i> '+esc(a.text)+'</p>';}).join(''):'<p>(none listed)</p>')+'</div></div>';
 h+='<h4>Sources ('+e.sources.length+')</h4><ul>'+e.sources.map(function(s){var u=s.doi?'https://doi.org/'+s.doi:s.url;return'<li>'+esc(s.authors?s.authors+' ('+s.year+'). ':'')+'<a href="'+esc(u)+'" target="_blank">'+esc(s.title)+'</a> ['+esc(s.type)+']</li>';}).join('')+'</ul>';content.innerHTML=h;side.classList.add('open');side.scrollTop=0;}
c.addEventListener('wheel',function(ev){ev.preventDefault();var r=c.getBoundingClientRect(),f=(c.width-(ev.clientX-r.left))/c.width,uc=uMin+f*(uMax-uMin),z=ev.deltaY>0?1.15:1/1.15;
 uMin=uc-(uc-uMin)*z;uMax=uc+(uMax-uc)*z;if(uMax-uMin<0.05){var m=(uMin+uMax)/2;uMin=m-.025;uMax=m+.025;}draw();},{passive:false});
var drag=null,moved=false;c.addEventListener('mousedown',function(ev){drag={x:ev.clientX,a:uMin,b:uMax};moved=false;});
window.addEventListener('mousemove',function(ev){if(!drag)return;var dx=ev.clientX-drag.x;if(Math.abs(dx)>3)moved=true;var du=dx/c.width*(drag.b-drag.a);uMin=drag.a+du;uMax=drag.b+du;draw();});
window.addEventListener('mouseup',function(ev){if(drag&&!moved){hitAt(ev.clientX,ev.clientY);}drag=null;});
function hitAt(cx,cy){var r=c.getBoundingClientRect(),mx=cx-r.left,my=cy-r.top;for(var i=0;i<hits.length;i++){var h=hits[i];if(mx>=h.x0-8&&mx<=h.x1&&my>=h.y0-10&&my<=h.y1+10){show(h.e);return;}}}
var t=null;function tinfo(ts){var r=c.getBoundingClientRect();if(ts.length>1)return{x:(ts[0].clientX+ts[1].clientX)/2-r.left,d:Math.abs(ts[0].clientX-ts[1].clientX)||1,n:2};return{x:ts[0].clientX-r.left,y:ts[0].clientY,n:1};}
c.addEventListener('touchstart',function(ev){ev.preventDefault();var i=tinfo(ev.touches);t={i:i,a:uMin,b:uMax,moved:t&&t.n===2?true:false,n:i.n,sx:ev.touches[0].clientX,sy:ev.touches[0].clientY};},{passive:false});
c.addEventListener('touchmove',function(ev){ev.preventDefault();if(!t)return;var i=tinfo(ev.touches),span=t.b-t.a;
 if(i.n!==t.i.n){t={i:i,a:uMin,b:uMax,moved:true,n:i.n};return;}
 if(i.n===2){var f0=(c.width-t.i.x)/c.width,uc=t.a+f0*span,ns=span*t.i.d/i.d;if(ns<0.05)ns=0.05;var f1=(c.width-i.x)/c.width;uMin=uc-f1*ns;uMax=uMin+ns;t.moved=true;}
 else{var dx=i.x-t.i.x;if(Math.abs(dx)>6)t.moved=true;var du=dx/c.width*span;uMin=t.a+du;uMax=t.b+du;}draw();},{passive:false});
c.addEventListener('touchend',function(ev){ev.preventDefault();if(t&&!t.moved&&ev.touches.length===0&&t.n===1)hitAt(t.sx,t.sy);if(ev.touches.length===0)t=null;else t={i:tinfo(ev.touches),a:uMin,b:uMax,moved:true,n:ev.touches.length>1?2:1};},{passive:false});
window.addEventListener('resize',resize);resize();
})();
