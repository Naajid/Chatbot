let sendbutton = document.getElementById('sendbutton')
sendbutton.addEventListener('click', buttonClickHandler);
sendbutton.addEventListener('keyup', keydown)
let messageslistnew1 = document.getElementById('messageslistnew1')
let messageslistnew2 = document.getElementById('messageslistnew2')
let messageslistnew3 = document.getElementById('messageslistnew3')
let messageslistnew4 = document.getElementById('messageslistnew4')
function buttonClickHandler(){
    console.log(document.getElementById('senderbutton').value)
    
    console.log('Button Clicked');


    let n = document.getElementById('form1')



    const xhr = new XMLHttpRequest();
    url = 'http://127.0.0.1:8000/botsearch/?question='
    url = url + (document.getElementById('senderbutton').value) ;
    // print(url);
    xhr.open('GET', url , true);
    xhr.onprogress = function(){
        console.log('On progress');
    }
    xhr.onload = function () {
       console.log("Onload Function running") 
       fetch('../static/sample.txt').then(
       response => response.text()).then(data => {
       element = document.getElementById("whatsapp");
        element.innerHTML = element.innerHTML + `<p class="messageslist"><img id="image" src="../static/bot3.jpeg" alt="bot" >${data}</p>`
    

       });
    }
    xhr.send();
    console.log("function completed running");
    n.reset();


   }

messageslistnew1.addEventListener('click', function buttonClickHandlernew1() {
    console.log("orders")
    const xhr = new XMLHttpRequest();
    url = 'http://127.0.0.1:8000/botsearch/?question='
    url = url + "orders" ;
    xhr.open('GET', url , true);
    xhr.onprogress = function(){
        console.log('On progress');
    }
    xhr.onload = function () {
       console.log("Onload Function running") 
       fetch('../static/sample.txt').then(
       response => response.text()).then(data => {
       element = document.getElementById("whatsapp");
        element.insertAdjacentHTML('beforeend', `<p class="messageslist"><img id="image" src="../static/bot3.jpeg" alt="bot" >${data}</p>`)
    

       });
    }
    xhr.send();
    console.log("function completed running");
    

    
});
messageslistnew3.addEventListener('click', function buttonClickHandlernew3() {
    console.log("complaints")

    const xhr = new XMLHttpRequest();
    url = 'http://127.0.0.1:8000/botsearch/?question='
    url = url + "complaints" ;
    xhr.open('GET', url , true);
    xhr.onprogress = function(){
        console.log('On progress');
    }
    xhr.onload = function () {
       console.log("Onload Function running") 
       fetch('../static/sample.txt').then(
       response => response.text()).then(data => {
       element = document.getElementById("whatsapp");
       element.insertAdjacentHTML('beforeend', `<p class="messageslist"><img id="image" src="../static/bot3.jpeg" alt="bot" >${data}</p>`)
    

       });
    }
    xhr.send();
    console.log("function completed running");
});
messageslistnew2.addEventListener('click', function buttonClickHandlernew2() {
    console.log("wishlist")

    const xhr = new XMLHttpRequest();
    url = 'http://127.0.0.1:8000/botsearch/?question='
    url = url + "wishlist" ;
    xhr.open('GET', url , true);
    xhr.onprogress = function(){
        console.log('On progress');
    }
    xhr.onload = function () {
       console.log("Onload Function running") 
       fetch('../static/sample.txt').then(
       response => response.text()).then(data => {
       element = document.getElementById("whatsapp");
       element.insertAdjacentHTML('beforeend', `<p class="messageslist"><img id="image" src="../static/bot3.jpeg" alt="bot" >${data}</p>`)
    

       });
    }
    xhr.send();
    console.log("function completed running");

});
messageslistnew4.addEventListener('click', function buttonClickHandlernew4() {
    console.log("executive")
    data = "Connected to the JGI BOT"
    element = document.getElementById("whatsapp");
    element.insertAdjacentHTML('beforeend', `<p class="messageslist"><img id="image" src="../static/bot3.jpeg" alt="bot" >${data}</p>`)

});




function keydown(e) {
    var x = e.keyCode;
    console.log('Function Keydown Called')
    if(x == 13){
    element = document.getElementById("whatsapp");
    
    
    element.innerHTML = element.innerHTML + ` <p class="messageslist" id="usermessage">${document.getElementById('senderbutton').value}<img id="image" src="../static/user.jpeg" alt="bot" ></p>`
    buttonClickHandler()
    
    }
}






