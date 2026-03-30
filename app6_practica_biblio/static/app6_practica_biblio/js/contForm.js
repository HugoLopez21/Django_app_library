
//Genera el dni cuando se presiona el boton 
document.getElementById('btn-dni').addEventListener("click", () => {
    
    let numero = Math.floor(Math.random() * 100000000);
    let numeroStr = numero.toString().padStart(8, '0'); // rellenar con ceros a la izquierda

    const letras = "TRWAGMYFPDXBNJZSQVHLCKE";
    const letra = letras[numero % 23];
    const dni = numeroStr + letra;
    
    document.getElementById('dni').value = dni;
}) 

//Muestra unicamente el carnet del socio que se seleccione.
function mostrarSocioSelec(){

    const socio = document.getElementById("socio").value; 
    fetch(`mostrar_socio_seleccionado/?socio=${socio}`) //Llama a la vista pasandole como parametro al socio
        .then(response => response.text())
        .then(data => {
            document.querySelector(".der").innerHTML = data; //Añade al div "der" el carnet generado en el servidor
        })
        .catch(error => console.error("Error:", error));  
    };

function mostrarSocios(){
    /* 
    Esta funcion recoge que opcion de orden está seleccionada,
    la envia al servidor y el servidor devuelve todos los carnets
    según el orden.
     */

    const opciones = document.getElementsByName("orden");
    let orden = null;
    for (let radio of opciones) {
        if (radio.checked) {
            orden = radio.value;
            break;
        };
    };

fetch(`mostrar_socios/?orden=${orden}`)
    .then(response => response.text())
    .then(data => {
        document.querySelector(".der").innerHTML = data; 
    })
    .catch(error => console.error("Error:", error));  
};


//Al clickar el boton se envia el formulario por post
document.getElementById('form-alta').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    //Definimos la cabecera
    const form = e.target;
    const url = form.action; //Recoge del html la url de la vista
    const formData = new FormData(form);
    const response = await fetch(url, {method: 'POST', body: formData});

    if (response.ok) {
        const html = await response.text(); //Recibe la respuesta de la vista
        //Añadimos al div de contenido los datos generados
        document.querySelector('.der').innerHTML = html; 
        form.reset(); //Quita contenido del formulario
    };
});



 
    