let current_version;
let control_version;
const change = [];

alert(change.length);

function version_control() {
    console.log(change.length)
}

function undo(context) {
    //if current is in range
    alert();
    control_version = current_version - 1
    c.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    document.getElementById('photo_edited').value = image_co_data;
    var img = new Image;
    img.src = image_co_data;
    c.getContext('2d').drawImage(img, 0, 0, sessionStorage.getItem("imgWidth"), sessionStorage.getItem("imgHeight"));
}

function redo() {
    alert();
    //ifin current range
    control_version = current_version + 1
}

// version_control();