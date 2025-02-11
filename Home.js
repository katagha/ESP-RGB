// this funtion will send the collor selected and send it to the server 

function SendColor ()

{

    Color_Selected =document.getElementById("color").value;
    
    fetch('127.0.0.1:8080', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ COLOR: Color_Selected }) 
    })
    .catch(error => console.error(error));



    
}