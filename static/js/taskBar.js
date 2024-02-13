var i = 0;
function move(timeStamp) {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = timeStamp * 100;
    var id = setInterval(frame, 8);
    function frame() {
      if (width <= 0) {
        clearInterval(id);
        i = 0;
        console.log("END!")
      } else {
        width--;
        elem.style.width = (width/timeStamp) + "%";
      }
    }
  }
}