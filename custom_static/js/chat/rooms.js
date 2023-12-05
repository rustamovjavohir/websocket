console.log("Sanity check from room.js.");

// focus 'roomInput' when user opens the page
document.querySelector("#roomInput").focus();

// submit if the user presses the enter key
document.querySelector("#roomInput").onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter key
        document.querySelector("#roomConnect").click();
    }
};

// redirect to '/room/<roomInput>/'
document.querySelector("#roomConnect").onclick = function () {
    let roomName = document.querySelector("#roomInput").value;
    window.location.pathname = "chat/rooms/" + roomName + "/";
}

// redirect to '/room/<roomSelect>/'
document.querySelector("#roomSelect").onchange = function () {
    let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
    window.location.pathname = "chat/rooms/" + roomName + "/";
}


// slideBarShow();

let slideBar= localStorage.getItem("slidebar") || 'hide';

if (slideBar === "show") {
    document.getElementById("nav-bar").classList.add("show");
    document.getElementById("header-toggle").classList.add("bx-x");
    document.getElementById("body-pd").classList.add("body-pd");
    document.getElementById("header").classList.add("body-pd");
}