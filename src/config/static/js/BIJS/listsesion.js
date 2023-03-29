import Axios from 'axios';
divcategory = document.getElementById('tablas')
function listcategory(){
  Axios.get('/viewlistcategory', {
    responseType: 'json'
})
.then(function(response) {
    const datos = response.data
    let category = '';
    for (let id in datos) {
      category += `<div class="div-table-row">
      <div class="div-table-cell">${id}</div>
      <div class="div-table-cell">${datos.N_cat}</div>
      <div class="div-table-cell">${datos.Descripcion}</div>
      <div class="div-table-cell">  
          <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
      </div>
      <div class="div-table-cell">
          <button class="btn btn-danger"><i class="zmdi zmdi-delete"></i></button>
      </div>
  </div>`;
    }
    divcategory.innerHTML = category
})
.catch(function(err) {
    console.log(err);
})
.then(function() {});

}

