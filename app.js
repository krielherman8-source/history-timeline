(function(){
var D=window.TIMELINE_DATA,c=document.getElementById('c'),x=c.getContext('2d'),side=document.getElementById('side'),content=document.getElementById('content');
document.getElementById('close').onclick=function(){side.classList.remove('open');};
var NOW=new Date().getFullYear();
function toU(y){return Math.log10(Math.max(NOW-y,1));} // u = log10(years ago)
var U_LO=-0.2,U_HI=10.4,MIN_SPAN=0.002,MAX_SPAN=U_HI-U_LO;
var uMin=U_LO,uMax=U_HI,W=0,H=0,hits=[],raf=0;
function clamp(){var s=uMax-uMin;if(s<MIN_SPAN){var m=(uMin+uMax)/2;uMin=m-MIN_SPAN/2;uMax=m+MIN_SPAN/2;s=MIN_SPAN;}
 if(s>MAX_SPAN){uMin=U_LO;uMax=U_HI;return;}if(uMin<U_LO){uMax+=U_LO-uMin;uMin=U_LO;}if(uMax>U_HI){uMin-=uMax-U_HI;uMax=U_HI;}}
function px(u){return W-(u-uMin)/(uMax-uMin)*W;} // past on the left
function uAt(p){return uMin+(W-p)/W*(uMax-uMin);}
function zoomAt(p,f){var uc=uAt(p);uMin=uc-(uc-uMin)*f;uMax=uc+(uMax-uc)*f;clamp();req();}
function req(){if(!raf)raf=requestAnimationFrame(function(){raf=0;draw();});}
function resize(){var r=c.parentNode.getBoundingClientRect(),d=window.devicePixelRatio||1;W=r.width;H=r.height;
 c.style.width=W+'px';c.style.height=H+'px';c.width=Math.round(W*d);c.height=Math.round(H*d);x.setTransform(d,0,0,d,0,0);draw();}
var ST={confirmed:['#5d8','Confirmed'],disputed:['#fb4','Disputed'],hypothesis:['#ff7','Hypothesis'],debunked:['#f55','Debunked / hoax'],'myth-legend':['#c9f','Myth / legend']};
var CAL=1e5; // below this many years ago, ticks/labels use round calendar years
function lbl(t){if(t.y!=null)return t.y<0?(-t.y)+' BCE':t.y+' CE';var ya=t.v;if(ya>=1e9)return+(ya/1e9).toPrecision(3)+' Bya';if(ya>=1e6)return+(ya/1e6).toPrecision(3)+' Mya';return+(ya/1e3).toPrecision(4)+' kya';}
function ticks(){var a=Math.pow(10,Math.max(uMin,0)),b=Math.pow(10,uMax),out=[],seen={};
 for(var p=Math.ceil(uMax);p>=0;p--){[1,5,2].forEach(function(m){var s=m*Math.pow(10,p);
  var cal=s<CAL; // calendar-year grid
  var lo=cal?NOW-Math.min(b,CAL):Math.max(a,CAL),hi=cal?NOW-a:b;if(lo>hi)return;
  var vals=[];if((hi-lo)/s<=300){for(var v=Math.ceil(lo/s)*s;v<=hi;v+=s)vals.push(v);}
  else for(var k=-9;k<10;k++){var v2=k*s;if(v2>=lo&&v2<=hi)vals.push(v2);}
  vals.forEach(function(v){var key=(cal?'y':'a')+v;if(seen[key])return;seen[key]=1;
   out.push(cal?{y:v===0?1:v,u:Math.log10(Math.max(NOW-(v===0?1:v),1))}:{v:v,u:Math.log10(v)});});});}
 return out;} // coarse->fine: rounder values claim label space first
function draw(){x.setTransform(window.devicePixelRatio||1,0,0,window.devicePixelRatio||1,0,0);x.fillStyle='#000';x.fillRect(0,0,W,H);
 var L=Math.round(H/2)+0.5;hits=[];
 x.strokeStyle='#fff';x.lineWidth=2;x.beginPath();x.moveTo(0,L);x.lineTo(W,L);x.stroke();x.lineWidth=1;
 x.font='11px sans-serif';x.textAlign='center';x.textBaseline='alphabetic';var used=[],GAP=10;
 ticks().forEach(function(t){var p=px(t.u);if(p<2||p>W-2)return;var s=lbl(t),w=x.measureText(s).width;
  if(p-w/2<0||p+w/2>W)return;
  for(var i=0;i<used.length;i++)if(Math.abs(used[i][0]-p)<(used[i][1]+w)/2+GAP)return;used.push([p,w]);
  x.strokeStyle='#aaa';x.beginPath();x.moveTo(Math.round(p)+.5,L-7);x.lineTo(Math.round(p)+.5,L);x.stroke();x.fillStyle='#ddd';x.fillText(s,p,L-11);});
 x.textAlign='left';x.font='12px sans-serif';var labels=[],rows=[],RH=18,maxRows=Math.max(2,Math.floor((H/2-28-150)/RH)+1);
 var eff=(uMax-uMin)*390/Math.max(W,1),level=eff>6?1:eff>2.5?2:3;
 D.entries.slice().sort(function(m,n){return(m.priority||2)-(n.priority||2)||m.start-n.start;}).forEach(function(e){var a=px(toU(e.start)),b=e.end!=null?px(toU(e.end)):a;
  if(Math.max(a,b)<-200||Math.min(a,b)>W+10)return;
  var pr=e.priority||2,show=pr<=level,col=(ST[e.status]||['#ccc'])[0],myth=e.lane==='myth',R=show?6:3.5;x.fillStyle=col;
  if(show&&b-a>2){x.globalAlpha=.4;x.fillRect(Math.max(a,0),L-3,Math.min(b,W)-Math.max(a,0),6);x.globalAlpha=1;}
  x.beginPath();if(myth){x.moveTo(a,L-R-1);x.lineTo(a+R+1,L);x.lineTo(a,L+R+1);x.lineTo(a-R-1,L);}else x.arc(a,L,R,0,7);x.fill();
  if(!show){hits.push({e:e,x0:a-8,x1:a+8,y0:L-10,y1:L+10,ax:a});return;}
  var w=x.measureText(e.title).width,lx=Math.max(4,Math.min(a-6,W-w-4)),r=0;while(r<maxRows&&rows[r]!=null&&rows[r]>lx-6)r++;
  if(r>=maxRows){hits.push({e:e,x0:a-8,x1:a+8,y0:L-10,y1:L+10,ax:a});return;} // no room: marker only
  rows[r]=lx+w;var y=L+28+r*RH;
  x.strokeStyle='#555';x.beginPath();x.moveTo(a,L+R+1);x.lineTo(a,y-11);x.stroke();labels.push([e.title,lx,y,w]);
  hits.push({e:e,x0:Math.min(a-10,lx),x1:Math.max(a+10,lx+w),y0:L-12,y1:y+5,ax:a});});
 labels.forEach(function(l){x.fillStyle='#000';x.fillRect(l[1]-2,l[2]-12,l[3]+4,16);x.fillStyle='#eee';x.fillText(l[0],l[1],l[2]);});
 x.font='11px sans-serif';var ks=Object.keys(ST),ly=H-12-ks.length*15-30;
 ks.forEach(function(k,i){x.fillStyle=ST[k][0];x.fillRect(9,ly+i*15-8,9,9);x.fillStyle='#ccc';x.fillText(ST[k][1],24,ly+i*15);});
 ly+=ks.length*15+6;x.fillStyle='#ccc';x.beginPath();x.arc(13,ly-4,4.5,0,7);x.fill();x.fillText('History / science',24,ly);
 ly+=15;x.beginPath();x.moveTo(13,ly-9);x.lineTo(18,ly-4);x.lineTo(13,ly+1);x.lineTo(8,ly-4);x.fill();x.fillText('Myth / legend lane',24,ly);
 x.fillStyle='#888';x.textAlign='right';x.fillText(level<3?'Zoom in for more entries':'',W-8,H-10);x.textAlign='left';}
function esc(s){return String(s).replace(/[&<>"]/g,function(ch){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch];});}
function yr(v){return v<0?-v+' BCE':v+' CE';}
function show(e){var s=ST[e.status]||['#ccc',e.status];var h='<h3>'+esc(e.title)+'</h3><div><span class="badge" style="background:'+s[0]+'">'+esc(s[1])+'</span>'+e.evidenceTypes.map(function(t){return'<span class="tag">'+esc(t)+'</span>';}).join('')+'</div>';
 h+='<p><b>Date:</b> '+yr(e.start)+(e.end!=null?' – '+yr(e.end):'')+(e.dateNote?' <i>('+esc(e.dateNote)+')</i>':'')+'</p>';
 h+='<div class="cols"><div><b>Mainstream view</b><p>'+esc(e.mainstream)+'</p></div><div><b>Alternative views</b>'+(e.alternatives.length?e.alternatives.map(function(a){return'<p><i>'+esc(a.label)+':</i> '+esc(a.text)+'</p>';}).join(''):'<p>(none listed)</p>')+'</div></div>';
 if(e.changed)h+='<div class="changed"><b>How understanding changed</b><p>'+esc(e.changed)+'</p></div>';
 var md=e.media||[];md.forEach(function(m){if(m.type==='image')h+='<figure><img src="'+esc(m.url)+'" alt="'+esc(m.title)+'" loading="lazy"><figcaption>'+esc(m.author)+', <a href="'+esc(m.page)+'" target="_blank" rel="noopener">'+esc(m.license)+', via Wikimedia Commons</a></figcaption></figure>';});
 md.forEach(function(m){if(m.type==='video')h+='<p class="vid">&#9654; <a href="'+esc(m.url)+'" target="_blank" rel="noopener">'+esc(m.title)+'</a><br><small>YouTube: '+esc(m.channel)+'</small></p>';});
 h+='<h4>Sources ('+e.sources.length+')</h4><ul>'+e.sources.map(function(s){var u=s.doi?'https://doi.org/'+s.doi:s.url;return'<li>'+esc(s.authors?s.authors+' ('+s.year+'). ':'')+'<a href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(s.title)+'</a> ['+esc(s.type)+']</li>';}).join('')+'</ul>';
 content.innerHTML=h;side.classList.add('open');side.scrollTop=0;}
function hitAt(cx,cy){var r=c.getBoundingClientRect(),mx=cx-r.left,my=cy-r.top,best=null,bd=1e9;
 hits.forEach(function(h){if(mx>=h.x0&&mx<=h.x1&&my>=h.y0&&my<=h.y1){var d=Math.abs(mx-h.ax);if(d<bd){bd=d;best=h;}}});if(best)show(best.e);}
c.addEventListener('wheel',function(ev){ev.preventDefault();var r=c.getBoundingClientRect(),dy=ev.deltaMode===1?ev.deltaY*16:ev.deltaY;
 zoomAt(ev.clientX-r.left,Math.exp(Math.max(-1,Math.min(1,dy/300))));},{passive:false});
var drag=null;c.addEventListener('mousedown',function(ev){drag={x:ev.clientX,a:uMin,b:uMax,moved:false};c.style.cursor='grabbing';});
window.addEventListener('mousemove',function(ev){if(!drag)return;var dx=ev.clientX-drag.x;if(Math.abs(dx)>3)drag.moved=true;var du=dx/W*(drag.b-drag.a);uMin=drag.a+du;uMax=drag.b+du;clamp();req();});
window.addEventListener('mouseup',function(ev){if(drag&&!drag.moved)hitAt(ev.clientX,ev.clientY);drag=null;c.style.cursor='';});
var t=null;
function tstate(ts){var r=c.getBoundingClientRect();if(ts.length>1){var dx=ts[0].clientX-ts[1].clientX,dy=ts[0].clientY-ts[1].clientY;
 return{n:2,x:(ts[0].clientX+ts[1].clientX)/2-r.left,d:Math.max(Math.hypot(dx,dy),10)};}return{n:1,x:ts[0].clientX-r.left};}
function tbegin(ev,moved){t={s:tstate(ev.touches),a:uMin,b:uMax,moved:moved,sx:ev.touches[0].clientX,sy:ev.touches[0].clientY};}
c.addEventListener('touchstart',function(ev){ev.preventDefault();tbegin(ev,!!t);},{passive:false});
c.addEventListener('touchmove',function(ev){ev.preventDefault();if(!t)return;var s=tstate(ev.touches);if(s.n!==t.s.n){tbegin(ev,true);return;}
 var span=t.b-t.a;if(s.n===2){var uc=t.a+(W-t.s.x)/W*span,ns=span*t.s.d/s.d;ns=Math.max(MIN_SPAN,Math.min(MAX_SPAN,ns));uMin=uc-(W-s.x)/W*ns;uMax=uMin+ns;t.moved=true;}
 else{var dx=s.x-t.s.x;if(Math.abs(dx)>8)t.moved=true;var du=dx/W*span;uMin=t.a+du;uMax=t.b+du;}clamp();req();},{passive:false});
c.addEventListener('touchend',function(ev){ev.preventDefault();if(!t)return;if(ev.touches.length===0){if(!t.moved)hitAt(t.sx,t.sy);t=null;}else tbegin(ev,true);},{passive:false});
c.addEventListener('touchcancel',function(){t=null;});
window.addEventListener('resize',resize);
window.TL={view:function(a,b){if(a!=null){uMin=a;uMax=b;clamp();draw();}return[uMin,uMax];},yearToU:toU};
resize();
})();
