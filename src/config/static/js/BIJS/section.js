var row="";
var filas = [1,2,3];
function viewSectionEdad() {
    const addOptionEdad = document.getElementById('addOptionEdad');
    for (let iterar = 0; iterar < filas.length; iterar++) {
        row += `<option value="${iterar++}° año">${iterar}°</option>`
        iterar--
        filas.push(row);
    }    
    addOptionEdad.innerHTML = row;
}

function addSection() {
  const addOptionEdad = document.getElementById('addOptionEdad');
  row += `<option value="1° año ">1°</option>`
              /*<th scope="row">${addOptionEdad.value}</th>
              <td>${descripcion.value}</td>
            </tr>*/
  filas.push(row);

  //addr.innerHTML = row;
  
  row= `<tr class=${filas.length %2 == 0? "table-success": "table-danger"}>
              <th scope="row">${addOptionEdad.value}</th>
              <td>${descripcion.value}</td>
              <td><a class="btn btn-primary">actualizar</a></td>
              <td><a class="btn btn-danger">Eliminar</a></td>
            </tr>`;
  filas.push(row);
  addr.innerHTML = row;
}

/*
const selpokemon = document.getElementById('pokemon');
const divpokeimagen = document.getElementById('pokeimagen');
//const axios = require('axios');


selpokemon.addEventListener('change', function() {
    alertify.success(''+this.value);
   //creamos nuestro endpoint
    let endpoint = `https://pokeapi.co/api/v2/pokemon/${this.value}`;
    //alertify.success(endpoint);
    // Hacer una petición para un usuario con ID especifico
    axios.get(endpoint)
    .then(function (response) {
        // manejar respuesta exitosa
        //console.log(response.data.sprites);
        const sprite = response.data.sprites
        let tarjetas= '';

        for (let item in sprite) {
            if(item == "back_default" || item == "front_default" ){
                console.log(sprite[item]);
                let urlimg = sprite[item];
                tarjetas +=`<div class="col">
                                <div class="card">
                                    <img src="${urlimg}" class="card-img-top" alt="...">
                                    <div class="card-body">
                                        <h5 class="card-title">${item}</h5>
                                        <p class="card-text">
                                        </p>
                                    </div>
                                </div>
                            </div>`;
                
            console.log('paso por la tarjeta');
            }            
        }
        divpokeimagen.innerHTML = tarjetas
       
        
    })
    .catch(function (error) {
        // manejar error
        console.log(error);
    })
    .finally(function () {
        // siempre sera executado
        console.log('ejecucción finalizada');
    });

}, false);

function GuardarAdministrador() {
    const nameadmin = document.getElementById('nombreadmin');
    const emailadmin = document.getElementById('emailadmin');
    const usernameadmin = document.getElementById('usernameadmin');
    const passadmin = document.getElementById('passadmin');
    const passadmin2 = document.getElementById('passadmin2');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardaradmin', {
        fullname: nameadmin.value,
        Email: emailadmin.value
        //orders: [1, 2, 3],
        //photo: document.querySelector('#fileInput').files
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}

var codMunicipios = new Array();
var idEstado =  new Array();
var municipios = new Array();

function limpiarMunicipios() {
    var reference = document.frmCombos.cmbMunicipios;
    var largo = reference.options.length;
    for ( j = 0; j < 8; j++ ){
        for ( i = 0; i < largo; i++ ){
            document.frmCombos.cmbMunicipios.remove(i);
        }
    }
}

function cargarMunicipios(valor) {
    var longitud = idEstado.length;
    var reference = document.frmCombos.cmbMunicipios;
    var i = 0;
    var j = 0;
    
    limpiarMunicipios();
    
    for ( i = 0; i < longitud; i++ ) {
            if ( idEstado[i] == valor ) {
                var newOption = new Option(municipios[i], codMunicipios[i]);
                reference.options[j] = newOption;
                j++;
            }
    }
    document.frmCombos.totalMunicipios.value = j + ' municipios';
}*/