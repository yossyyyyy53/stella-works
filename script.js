// ---- works grid: brief motion before navigating to a detail page ----
document.querySelectorAll('.card:not(.is-disabled)').forEach(function(card){
  card.addEventListener('click', function(e){
    var href = card.getAttribute('href');
    if(!href) return;
    e.preventDefault();
    if(card.classList.contains('is-active')) return;
    card.classList.add('is-active');
    setTimeout(function(){ window.location.href = href; }, 260);
  });
});

// ---- back to top button ----
var backBtn = document.querySelector('.back-to-top');
if(backBtn){
  var toggle = function(){
    if(window.scrollY > 240){
      backBtn.classList.add('is-visible');
    }else{
      backBtn.classList.remove('is-visible');
    }
  };
  window.addEventListener('scroll', toggle, {passive:true});
  toggle();
  backBtn.addEventListener('click', function(){
    window.scrollTo({top:0, behavior:'smooth'});
  });
}
