  const form=document.getElementById('form-b');
  const confirmation=document.getElementById('confirmation');
  const montrerConfirmation=()=>{form.classList.add('envoye');confirmation.hidden=false;confirmation.focus({preventScroll:true});confirmation.scrollIntoView({block:'center',behavior:'smooth'})};
  document.getElementById('b-autre')?.addEventListener('click',()=>{form.classList.remove('envoye');confirmation.hidden=true;form.elements.nom.focus()});
  if(form) form.addEventListener('submit',e=>{e.preventDefault();document.getElementById('confirmation-texte').textContent="Maquette : aucun e-mail n'est envoyé depuis cette version.";montrerConfirmation()});
