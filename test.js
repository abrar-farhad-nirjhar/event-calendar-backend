


let endpoint = 'ws://'+'127.0.0.1:8000/eventConsumer/'
let socket = new WebSocket(endpoint)
console.log(window.location)

socket.onmessage = function(e){
    console.log("message", e)
    
}
socket.onopen = function(e){
    console.log("message", e)
    document.getElementById('iii').addEventListener('click',(event)=>{
        socket.send("hello")
    })
    
}


socket.onerror = function(e){
    console.log("message", e)
}
socket.onclose = function(e){
    console.log("message", e)
}