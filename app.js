'use strict';
const buttons=[...document.querySelectorAll('[data-filter]')];
const cards=[...document.querySelectorAll('[data-category]')];
buttons.forEach(button=>button.addEventListener('click',()=>{
 const filter=button.dataset.filter;let count=0;
 buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 cards.forEach(card=>{card.hidden=filter!=='todos'&&card.dataset.category!==filter;if(!card.hidden)count++;});
 document.getElementById('filter-status').textContent=`${count} projeto${count===1?'':'s'} exibido${count===1?'':'s'}`;
}));
