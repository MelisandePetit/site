  // Envoi du formulaire de devis par e-mail (service Web3Forms)
  const form=document.getElementById('form-b'), info=document.getElementById('merci-b'), bouton=document.getElementById('b-envoyer');
  const libelle=bouton?bouton.innerHTML:'';
  const confirmation=document.getElementById('confirmation');
  const montrerConfirmation=()=>{form.classList.add('envoye');confirmation.hidden=false;confirmation.focus({preventScroll:true});confirmation.scrollIntoView({block:'center',behavior:'smooth'})};
  document.getElementById('b-autre')?.addEventListener('click',()=>{form.classList.remove('envoye');confirmation.hidden=true;form.elements.nom.focus()});
  if(form) form.addEventListener('submit',async e=>{
    e.preventDefault();
    const v=n=>form.elements[n].value.trim();
    bouton.disabled=true; bouton.textContent='Envoi en cours…'; info.hidden=true;
    try{
      const r=await fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({
        access_key:'ced3a1aa-89b7-4208-9231-da04f29b1912',
        subject:'Demande de devis – '+v('nom'),
        from_name:'Site NG Façades',
        replyto:v('email'),
        botcheck:form.elements.botcheck.checked,
        'Nom et prénom':v('nom'),
        'Téléphone':v('telephone')||'non indiqué',
        email:v('email'),
        'Type de bâtiment':v('batiment'),
        'Travaux souhaités':v('travaux'),
        'Message':v('message')||'(aucun message)'
      })});
      const d=await r.json();
      if(!r.ok||!d.success) throw new Error(d.message||'envoi refusé');
      form.reset();
      montrerConfirmation();
    }catch(err){
      info.textContent="L'envoi n'a pas fonctionné. Appelez-nous au +41 78 230 28 41 ou écrivez-nous à info@ngfacades.ch.";
      info.hidden=false;
    }
    bouton.disabled=false; bouton.innerHTML=libelle;
  });
