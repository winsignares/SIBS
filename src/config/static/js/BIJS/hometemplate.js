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
  
  var encabezado = document.getElementById("encabezado");
var enlace = document.getElementById("enlace");

// Función para mostrar el contenido del iframe
function mostrarContenido() {
  // Ocultar todos los mosaicos
  var tiles = document.getElementsByClassName("tile");
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "none";
  }

  // Mostrar el contenido del iframe y el enlace, y ocultar el encabezado
  var contenidoAdmin = document.getElementById("contenidoAdmin");
  contenidoAdmin.style.display = "block";
  enlace.style.display = "block";
  encabezado.style.display = "none";

  // Crear nuevo elemento de encabezado
  var nuevoEncabezado = document.createElement("h1");
  nuevoEncabezado.classList.add("all-tittles");
  var textoEncabezado = document.createTextNode("Administradores");
  nuevoEncabezado.appendChild(textoEncabezado);
  enlace.parentNode.insertBefore(nuevoEncabezado, enlace.nextSibling);

  // Animar el iframe correspondiente hacia arriba
  contenidoAdmin.style.transform = "translateY(100%)";
  contenidoAdmin.animate([
    { transform: "translateY(100%)" },
    { transform: "translateY(0)" }
  ], {
    duration: 500,
    easing: "ease-in-out"
  }).onfinish = function() {
    contenidoAdmin.style.transform = "";
  };
}

// Función para ocultar el contenido del iframe y eliminar el nuevo encabezado
function ocultarContenido() {
  // Ocultar el contenido del iframe y el enlace, y mostrar el encabezado
  var contenidoAdmin = document.getElementById("contenidoAdmin");
  contenidoAdmin.style.display = "none";
  enlace.style.display = "none";
  encabezado.style.display = "block";

  // Eliminar el nuevo encabezado
  var nuevoEncabezado = enlace.nextSibling;
  if (nuevoEncabezado && nuevoEncabezado.tagName == "H1") {
    nuevoEncabezado.parentNode.removeChild(nuevoEncabezado);
  }

  // Mostrar todos los mosaicos
  var tiles = document.getElementsByClassName("tile");
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].style.display = "block";
  }
}


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

  
  
  

  

 
  