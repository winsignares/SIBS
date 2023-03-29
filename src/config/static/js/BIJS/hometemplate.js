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
  function mostrarContenido(id) {
    // Ocultar todos los mosaicos
    var tiles = document.getElementsByClassName("tile");
    for (var i = 0; i < tiles.length; i++) {
      tiles[i].style.display = "none";
    }
  
    // Mostrar el iframe correspondiente
    var contenido = document.getElementById(id);
    contenido.style.display = "block";
  }
  
  function ocultarContenido(id) {
    // Ocultar el iframe correspondiente
    var contenido = document.getElementById(id);
    contenido.style.display = "none";
  
    // Mostrar todos los mosaicos
    var tiles = document.getElementsByClassName("tile");
    for (var i = 0; i < tiles.length; i++) {
      tiles[i].style.display = "block";
    }
  }
  
  // Agregar clase de posición original a cada tile
var tiles = document.getElementsByClassName("tile");
for (var i = 0; i < tiles.length; i++) {
  tiles[i].classList.add("original-position-" + i);
}

// Función para restablecer la posición original de los tiles
function resetTilePositions() {
  var tiles = document.getElementsByClassName("tile");
  for (var i = 0; i < tiles.length; i++) {
    var originalPositionClass = "original-position-" + i;
    if (tiles[i].classList.contains(originalPositionClass)) {
      tiles[i].style.top = "";
      tiles[i].style.left = "";
    }
  }
}

// Llamar a la función resetTilePositions() cuando se haga clic en el botón "volver"
var volverButton = document.getElementById("volverButton");
volverButton.addEventListener("click", resetTilePositions);

  
  

  

 
  