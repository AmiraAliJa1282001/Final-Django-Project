var myNav = document.getElementById('mynav');
window.onscroll = function () { 
    if (document.body.scrollTop >= 10 ) {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};