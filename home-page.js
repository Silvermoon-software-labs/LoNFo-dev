function openForm(){
  var addClass = document.getElementsByClassName('form-wrapper')[0];
  addClass.classList.add("show-form");
}
function closeForm(){
  var addCloseClass = document.getElementsByClassName('form-wrapper')[0];
  addCloseClass.classList.remove("show-form");
}