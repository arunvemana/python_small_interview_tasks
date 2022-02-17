function alertwindow(elem)  {
    document.querySelector('.bg-modal').style.display = "flex";
    document.getElementById('ModleStockName').innerText =elem.id
    document.getElementById('ModelStockID').value = elem.id
    };
//document.getElementById('button').addEventListener("click", function() {

//});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});

//document.forms['QuestionForm'].addEventListener('submit', (event) => {
//    event.preventDefault();
//    document.getElementById('Message').text("adding to queue").show().fadeout(1000);
//    // TODO do something here to show user that form is being submitted
//    fetch(event.target.action, {
//        method: 'POST',
//        body: new URLSearchParams(new FormData(event.target)) // event.target is the form
//    }).then((resp) => {
//        return resp.json(); // or resp.text() or whatever the server sends
//    }).then((body) => {
//          event.su
//
//        // TODO handle body
//    }).catch((error) => {
//        // TODO handle error
//        document.getElementById('Message').text("failed...").show().fadeout(1000);
//
//    });
//});