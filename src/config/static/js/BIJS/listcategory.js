


function listcategory() {
    const divcate = document.getElementById('tablas');
    axios.get('viewlist',{
        responseType: 'json'
    } )
      
      .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let categor = '';
            i= 0
            for (let index = 1; index < length; index++) {
                categor += `
                <div class="div-table-row">
                    <div class="div-table-cell">${datos[index].id}</div>
                    <div class="div-table-cell">${datos[index].cat}</div>
                    <div class="div-table-cell">${datos[index].descripcion}</div>
                    <div class="div-table-cell">
                        <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
                    </div>
                    <div class="div-table-cell">
                        <button class="btn btn-danger"><i class="zmdi zmdi-delete"></i></button>
                </div>
            </div>`;
                
            }
            divcate.innerHTML = categor        
      })
      .catch(function (error) {
        // Maneja los errores aquí
        console.log(error);
      });
  }
window.addEventListener('load', function() {
    listcategory();
})


