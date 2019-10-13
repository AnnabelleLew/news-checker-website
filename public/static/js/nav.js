function revealMenu(x) {
    var hidden = document.getElementById("small-hidden-nav");
    var menu = document.getElementsByClassName("menubar-nav")[0];
    if (hidden.style.display === "block") {
        hidden.style.display = "none";
        menu.style.height = "43px";
        menu.style.opacity = 1;
    } else {
        hidden.style.display = "block";
        menu.style.height = "100%";
        menu.style.opacity = 0.9;
    }
    x.classList.toggle("change")
}
