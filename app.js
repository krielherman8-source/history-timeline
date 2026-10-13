(function(){
var D=window.TIMELINE_DATA, c=document.getElementById('c'), x=c.getContext('2d'), side=document.getElementById('side'),content=document.getElementById('content');
document.getElementById('close').onclick=function(){side.classList.remove('open');};
var NOW=2026, toU=function(y){return Math.log10(Math.max(NOW-y,1))}; // u: log10 years ago (0..~10.14)
var uMin=0, uMax=10.3, hits=[];
function resize(){c.width=c.parentNode.clientWidth;c.height=c.parentNode.clientHeight;draw();}
function px(u){return c.width-(u-uMin)/(uMax-uMin)*c.width;} // past on left
function fmt(ya){return ya>=1e9?(ya/1e9).toFixed(1)+' Bya':ya>=1e6?(ya/1e6).toFixed(1)+' Mya':ya>=1e4?Math.round(ya/1e3)+' kya':(NOW-ya<0?Math.round(ya-NOW)+' BCE':Math.round(NOW-ya)+' CE');}
function draw(){x.clearRect(0,0,c.width,c.height);var H=c.height,lanes={history:H*0.35,myth:H*0.7};hits=[];
 x.fillStyle='#333';x.font='12px sans-serif';
 for(var u=Math.ceil(uMin*2)/2;u<=uMax;u+=0.5){var p=px(u);x.strokeStyle='#ddd';x.beginPath();x.moveTo(p,0);x.lineTo(p,H);x.stroke();x.fillText(fmt(Math.pow(10,u)),p+2,14);}
 for(var k in lanes){x.fillStyle='#000';x.font='bold 13px sans-serif';x.fillText(k==='myth'?'Myths & legends':'History / science',5,lanes[k]-40);x.strokeStyle='#999';x.beginPath();x.moveTo(0,lanes[k]);x.lineTo(c.width,lanes[k]);x.stroke();}
 var row={history:0,myth:0};
 D.entries.forEach(function(e){var y=lanes[e.lane]+((row[e.lane]++%3)*18)-20,a=px(toU(e.start)),b=e.end!=null?px(toU(e.end)):a+0;
  x.fillStyle=e.lane==='myth'?'#a4c':'#36a';x.fillRect(a-4,y,Math.max(b-a,0)+8,10);x.fillStyle='#000';x.font='12px sans-serif';x.fillText(e.title,a+8,y+9);
  hits.push({e:e,x0:a-6,x1:Math.max(b,a)+8+x.measureText(e.title).width,y0:y,y1:y+12});});}
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
