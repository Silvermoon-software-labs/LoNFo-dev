function openForm(){
  var addClass = document.getElementsByClassName('navbar-form')[0];
  var addRemoveClass = document.getElementsByClassName('close-btn')[0];
   var addClassforRemovingBtn = document.getElementsByClassName('btn-success')[0];
  addClass.classList.add("show-form");
  addRemoveClass.classList.add("show-close-button")
   addClassforRemovingBtn.classList.add("remove-sign-up")

}
function closeForm(){
  var addCloseClass = document.getElementsByClassName('navbar-form')[0];
 var remove = document.getElementsByClassName('show-form')[0];
 remove.classList.remove("remove-sign-up")
  addCloseClass.classList.remove("show-form");
}

window.onscroll = function(){
  stickyHeader();
} 

 var header = document.getElementsByClassName('header-wrapper')[0];
 var sticky = header.offsetTop;

function stickyHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}