var menuBtn = document.querySelector('.menu-btn');
var nav = document.querySelector('.navbar_m');
var lineOne = document.querySelector('.navbar_m .menu-btn .line--1');
var lineTwo = document.querySelector('.navbar_m .menu-btn .line--2');
var lineThree = document.querySelector('.navbar_m .menu-btn .line--3');
var link = document.querySelector('.navbar_m .nav-links');
menuBtn.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    lineOne.classList.toggle('line-cross');
    lineTwo.classList.toggle('line-fade-out');
    lineThree.classList.toggle('line-cross');
    link.classList.toggle('fade-in');
})
