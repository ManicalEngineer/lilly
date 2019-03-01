var menuBtn = document.getElementById("menu-btn");
var menu = document.getElementById("modal-menu")


window.onclick = function(e) {
	console.log(e.target.classList[1]);
	if (e.target.classList[1] !== "fa-navicon") {
		menu.style.visibility = "hidden";
	} else {
		menu.style.visibility = "visible";
	}
}