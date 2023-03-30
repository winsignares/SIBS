//function incorporarplantilla(id, ruta) {
    //const objto = document.getElementById(id);
    //fetch(ruta)
      //.then(response => response.text())
      //.then(data => {
     //objto.innerHTML = data;
      //})
      //.catch(error => {
       //console.error('Error al cargar el archivo:', error);
      //});
  //


  //function mostrarContenido(idContenido) {
    // Obtener la referencia al elemento div correspondiente al contenido
    //var contenido = document.getElementById(idContenido);
    
    // Obtener las referencias a los enlaces
    //var enlaces = document.querySelectorAll('.tile-name.all-tittles a');
    
    // Ocultar todos los contenidos excepto el que se quiere mostrar
    //for (var i = 0; i < enlaces.length; i++) {
      //var enlace = enlaces[i];
      //var idContenidoActual = enlace.getAttribute('href').substring(1);
      //var contenidoActual = document.getElementById(idContenidoActual);
      
      //if (idContenidoActual === idContenido) {
        // Si es el contenido que se quiere mostrar, se muestra
        //contenidoActual.style.display = 'block';
      //} else {
        // Si no es el contenido que se quiere mostrar, se oculta
        //contenidoActual.style.display = 'none';
      //}
    //}
  //}


  //function mostrarContenido(id) {
    // Ocultar todos los elementos con la clase "contenido-iframe"
    //var iframes = document.getElementsByClassName("contenido-iframe");
    //for (var i = 0; i < iframes.length; i++) {
      //iframes[i].style.display = "none";
    //}
  
    // Mostrar el elemento correspondiente
    //var contenido = document.getElementById(id);
    //contenido.style.display = "block";
  
    // Ocultar los demás enlaces
    //var tiles = document.getElementsByClassName("tile");
    //for (var i = 0; i < tiles.length; i++) {
      //var enlace = tiles[i].getElementsByTagName("a")[0];
      //if (enlace.getAttribute("href") != "#" + id) {
        //tiles[i].style.display = "none";
      //}
    //}
  //}
  
  // Guardar referencias a los elementos relevantes
var volverAtras = document.getElementById("volver-atras");
var contenidoAdmin = document.getElementById("contenidoAdmin");
var tiles = document.getElementsByClassName("tile");

// Agregar evento de clic al enlace "volver-atras"
volverAtras.addEventListener("click", function(event) {
  // Prevenir que se recargue la página
  event.preventDefault();

  // Ocultar el contenido del iframe y mostrar los mosaicos nuevamente
  contenidoAdmin.style.display = "none";
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "block";
  }
});

// Función para mostrar el contenido del iframe
function mostrarContenido(id) {
  // Ocultar todos los mosaicos
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "none";
  }
  
  // Animar el iframe correspondiente hacia arriba
  var contenido = document.getElementById(id);
  contenido.style.transform = "translateY(100%)";
  contenido.style.display = "block";
  contenido.animate([
    { transform: "translateY(100%)" },
    { transform: "translateY(0)" }
  ], {
    duration: 500,
    easing: "ease-in-out"
  }).onfinish = function() {
    contenido.style.transform = "";
  };
}

function animarEtiqueta() {
  var etiqueta = document.querySelector('.animacion');
  etiqueta.style.opacity = 0.1;
  etiqueta.style.fontSize = '10px';
}
function revertirAnimacion() {
  var etiqueta = document.querySelector('.animacion');
  etiqueta.style.opacity = 1;
  etiqueta.style.fontSize = '30px';
}
// Obtener el enlace de volver atrás
var enlaceVolver = document.getElementById("volver-atras");

// Agregar un evento de clic al enlace para ocultar el contenido
enlaceVolver.addEventListener("click", function(event) {
  event.preventDefault(); // Evitar que se actualice la página
  ocultarContenido("contenidoAdmin"); // Ocultar el contenido
});
function volverAtras() {
  // Retroceder una página en el historial del navegador
  window.history.back();
  // Desactivar el comportamiento predeterminado del enlace
  return false;
}
var volverAtrasLink = document.getElementById("volver-atras");

document.getElementById("indexadminLink").addEventListener("click", function() {
  volverAtrasLink.classList.remove("disabled-link");
});

volverAtrasLink.addEventListener("click", function(e) {
  e.preventDefault();
  ocultarContenido('contenidoAdmin');
});








//Este es un codigo llamativo
/*function mostrarContenido(id) {
  // Ocultar todos los mosaicos
  var tiles = document.getElementsByClassName("tile");
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "none";
  }

  // Ocultar el menú lateral
  var menuLateral = document.getElementsByClassName("container")[0];
  menuLateral.style.display = "none";

  // Mostrar el iframe correspondiente
  var contenido = document.getElementById(id);
  contenido.style.display = "block";
}

function ocultarContenido(id) {
  // Mostrar el menú lateralS
  var menuLateral = document.getElementsByClassName("container")[0];
  menuLateral.style.display = "block";

  // Ocultar el iframe correspondiente
  var contenido = document.getElementById(id);
  contenido.style.display = "none";

  // Mostrar todos los mosaicos
  var tiles = document.getElementsByClassName("tile");
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "block";
  }
}
*/

  
  
  

  

 
  