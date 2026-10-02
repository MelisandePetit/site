  const root=document.documentElement, burger=document.getElementById('burger');
  burger.addEventListener('click',()=>{const o=root.classList.toggle('menu-open');burger.setAttribute('aria-expanded',o)});
  document.querySelectorAll('.nav a').forEach(a=>a.addEventListener('click',()=>{root.classList.remove('menu-open');burger.setAttribute('aria-expanded',false)}));
  const track=document.getElementById('track');
  if(track){
    const step=()=>track.querySelector('.card').getBoundingClientRect().width+20;
    document.getElementById('next').onclick=()=>track.scrollBy({left:step(),behavior:'smooth'});
    document.getElementById('prev').onclick=()=>track.scrollBy({left:-step(),behavior:'smooth'});
  }
  document.getElementById('form-b').addEventListener('submit',e=>{e.preventDefault();document.getElementById('merci-b').hidden=false});
