var i = 0;
let question = document.querySelector(".quest");
let progressBar = document.querySelector(".myProgress");

function move(timeStamp) {
  if(progressBar.classList.contains("hiddenElement")){
    progressBar.classList.remove("hiddenElement")
  }
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = timeStamp * 100;
    var id = setInterval(frame, 8);
    function frame() {
      if (width <= 0) {
        clearInterval(id);
        i = 0;
        // console.log("END!")
        progressBar.classList.add("hiddenElement")
        question.classList.add("hiddenElement")
        socket.emit("endTime");
      } else {
        width--;
        elem.style.width = (width/timeStamp) + "%";
      }
    }
  }
}