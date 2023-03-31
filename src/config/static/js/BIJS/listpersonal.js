let morfismo = document.getElementById('poli');
let i = 0;

function viewpersonal() {
    axios.get('conpersonal',{
        responseType: 'json'
    } )
      
      .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let listper = '';
            i= 0
            for (let index = 1; index < length; index++) {
                listper += `
                    <div class="div-table" style="margin:0 !important;">
                        <div class="div-table-row div-table-row-list">
                        <div class="div-table-cell" style="width: 6%;">${index}</div>
                        <div id= "" class="div-table-cell" style="width: 15%;">${datos[index].dui}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].nombre}</div>
                        <div class="div-table-cell" style="width: 12%;">${datos[index].telefono}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].cargo}</div>
                        <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
                            </div>
                            <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-danger"><i class="zmdi zmdi-delete"></i></button>
                            </div>
                        </div>
                    </div>`;
            }
            morfismo.innerHTML = listper
        
      })
      .catch(function (error) {
        // Maneja los errores aquí
        console.log(error);
      });
  }

  
// function eliminarpersonal(){
//     const nose = document.getElementById('i');
//     //const id = nose.textContent;
//     axios.post('eliminarpersonal',{
//         id: nose.textContent, 
//     }, {
//         headers: {
//         'Content-Type': 'multipart/form-data'
//         }
//     }
//     ).then((res) => {
//         console.log(res.data)
//     })
//     .catch((error) => {
//         console.error(error)
    
//     })
// }