function incorporarplantilla(id, ruta) {
    const objto = document.getElementById(id);
    fetch(ruta)
      .then(response => response.text())
      .then(data => {
     objto.innerHTML = data;
      })
      .catch(error => {
       console.error('Error al cargar el archivo:', error);
      });
  }

  

 
  