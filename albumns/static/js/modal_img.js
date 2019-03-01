var doc = document;
var modal_frm = document.getElementById("modal-image");
var modal_cnt = document.getElementById("modal-content");



doc.onclick = function(e){
  console.log(e.target.classList);
  if (e.target.classList[0] == "imgs"){
    modal_frm.style.visibility = "visible";
    modal_cnt.children[1].src = e.target.src;
  }else if (e.target.classList[1] == "fa-times") {
    console.log("exit")
    modal_frm.style.visibility = "hidden";
  }
};
