function openForm(){
  var addClass = document.getElementsByClassName('navbar-form')[0];
  var addRemoveClass = document.getElementsByClassName('close-btn')[0];
   var addClassforRemovingBtn = document.getElementsByClassName('btn-success')[0];
   var hideMenu = document.getElementsByClassName('menu')[0];
  addClass.classList.add("show-form");
  addRemoveClass.classList.add("show-close-button")
   addClassforRemovingBtn.classList.add("remove-sign-up")
   hideMenu.classList.add("hide-menu"); 

}
function closeForm(){
  var addCloseClass = document.getElementsByClassName('navbar-form')[0];
 var remove = document.getElementsByClassName('show-form')[0];
 var showMenu = document.getElementsByClassName('menu')[0];
 remove.classList.remove("remove-sign-up")
  addCloseClass.classList.remove("show-form");
  showMenu.classList.remove('hide-menu');
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

function openNav() {
    document.getElementById("sidenav").style.width = "250px";
}

function closeNav(event) {
    document.getElementById("sidenav").style.width = 0;
    event.preventDefault(); //event bubbling & event capturing 
    event.stopPropagation();
    return false;
}
 var modal = document.getElementsByClassName("navbar-form");
window.onclick = function(event) {
  if (event.target === modal) {
      modal.style.display = "none";
  }
  else{
    modal.style.display = "none";
  }
}