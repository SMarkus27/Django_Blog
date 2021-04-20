const navToggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".links");
const searchBtn = document.querySelector(".btn-search");
const searchArea = document.querySelector(".search-area");

navToggle.addEventListener("click", function () {

  links.classList.toggle("show-links");
  
});

searchBtn.addEventListener('click',function(){

  searchArea.classList.toggle('search-form');
  searchBtn.classList.toggle('hidden-search');
  
});