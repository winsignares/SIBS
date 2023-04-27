


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
                <div class="table-responsive">
                <div class="div-table" style="margin:0 !important;">
                    <div class="div-table-row div-table-row-list">
                        <div class="div-table-cell" style="width: 6%;">#</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].id}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].cat}</div>
                        <div class="div-table-cell" style="width: 12%;">${datos[index].descripcion}</div>
                        <div class="div-table-cell" style="width: 9%;">
                            <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
                        </div>
                        <div class="div-table-cell" style="width: 9%;">
                            <a class="btn btn-danger"><i class="zmdi zmdi-delete"></i></a>
                        </div>
                    </div>
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


