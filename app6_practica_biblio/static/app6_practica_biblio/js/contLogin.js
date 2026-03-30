//Recoge datos de DOM
const botonLogin = document.getElementById("botonLogin");
const botonMuestraInfo = document.getElementById('visualiza');
const botonMuestraForm = document.getElementById('alta');
const body = document.body;
const divMid = document.getElementById('contenedor-mid');
const divDer = document.getElementById('contenedor-der');
const contenedorCarnets = document.getElementById('contenedor-carnets')

let estadoSesion = false;
let estadoForm = false;


function refrescaSesion(){
    //Llama a la vista para reestablecer el tiempo de sesión
    console.log('Refrescando sesión')
    fetch('refrescar_sesion');
};

body.addEventListener("click", function (elemento) {
    /*Evento en el body que distingue si se hace click sobre el boton de login/logout 
    para en caso de que el usuario esté activo se reestablezca el tiempo de sesíon
    */

    if (elemento.target.closest("#botonLogin") || !estadoSesion) {
        return;
    }
    refrescaSesion();
});



function verificarSesion(){
    /* 1. Ejecuta la vista donde se comprueba el tiempo de la sesion
        2. Recoge los datos de la vista
        3. si la sesion del server se ha acabado establece la variable del estado como falsa y cierra la sesion.
    */
   
    console.log('comprobando sesion');
    fetch('verificar_sesion')
        .then(response => response.json())
        .then(datos =>{
            if (datos.estadoSesion){
                estadoSesion = false;
                sesionLogout();
            };

        });
}
 
// Ejecuta la vista donde se destruye la variable de sesión y recoge el mensaje de estado de la petición
function limpiarSesion(){
    fetch('cerrar_sesion')
        .then(response => response.json())
        .then(datos =>{
            console.log('ejecución:' + datos.status + '\n' + datos.mensaje);
    });
};

function sesionLogin() {
    /*
    Esta funcion inicia la variable de sesión en el servidor y 
    comprueba si está activa cada 30 segundos
    */
    fetch('iniciar_sesion')
        .then(response => response.json())
        .then(datos => {
            console.log('ejecución:' + datos.status + '\n' + datos.mensaje)
            estadoSesion = true;
            if (datos.status === 'ok'){
                botonLogin.innerHTML = 'LOGOUT';
                botonLogin.onclick = sesionLogout;
                botonLogin.style.background = 'red';
                activaDesactiva();  
                
                /* Una vez comenzada la sesion cada 30 segundos, si el ultimo estado es activo, 
                verifica la sesion de nuevo.
                */

                setInterval(() => {
                    if(estadoSesion){
                        verificarSesion()
                    };
                   
                }, 30000);

                mostrarAlerta(datos.mensaje);
            };
        })
    };

function sesionLogout(){
    estadoSesion = false
    
    //Cambia el botón de login a logout
    botonLogin.innerHTML = 'LOGIN';
    botonLogin.onclick = sesionLogin;
    botonLogin.style.background = '#2ecc71';
    
    limpiarSesion();
    activaDesactiva();
    
    //Esconde el selector de socios
    document.getElementById('desplegable_visualizar').style.display = 'none'; 
    mostrarAlerta('ATENCIÓN: Sesión finalizada');
};

//Funcion que esconde o muestra el formulario
function activaDesactivaForm(){
    if (!estadoForm){
        estadoForm = true;
        document.getElementById('formulario').style.display = 'block';
        document.getElementById('desplegable_visualizar').style.display = 'none';
        
    }else{
        estadoForm = false;
        document.getElementById('formulario').style.display = 'none';
    };
};

//Funcion que esconde o muestra el selector de socios
function activaDesactivaVisua(){
    const contElementosVisua = document.getElementById('desplegable_visualizar');
    if (estadoSesion){
        if (contElementosVisua.style.display === 'none'){
            contElementosVisua.style.display = 'block';
            document.getElementById('formulario').style.display = 'none';
        }else{
            contElementosVisua.style.display = 'none';
        };
    };
};

//Activa o desactiva los botones de la sección de login
function activaDesactiva(){
    const contenedorElementos = document.getElementById('botonesLogin'); //Coge el div de los botones
    const elementos = contenedorElementos.querySelectorAll('input, select, button'); //Busca las etiquetas
    if (estadoSesion){
        //Si la sesión está activa habilita los botones
        elementos.forEach(element => element.disabled = false);
        
    }else{
        //Los deshabilita
        elementos.forEach(element => element.disabled = true);
        document.getElementById('formulario').style.display = 'none';
    };

};


//La funcion recoge un mensaje y la muestra en el contenedor derecho
function mostrarAlerta(mensaje){
    contenedorCarnets.innerHTML = `<h2>${mensaje}</h2>`
}