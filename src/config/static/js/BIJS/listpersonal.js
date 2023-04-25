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
                        <div class="div-table-cell  CC" style="width: 6%;">${index}</div>
                        <div id= "${i}" class="div-table-cell" style="width: 15%;">${datos[index].dui}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].nombre}</div>
                        <div class="div-table-cell" style="width: 12%;">${datos[index].telefono}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].cargo}</div>
                        <div class="div-table-cell" style="width: 9%;">
                                <a onclick="openModal()" class="btn btn-success"><i class="zmdi zmdi-refresh"></i></a>
                            </div>
                            <div class="div-table-cell" style="width: 9%;">
                                <a onclick= "eliminarper(this)" class="btn btn-danger"><i class="zmdi zmdi-delete"></i></a>
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
 
  window.addEventListener('load', function() {
    viewpersonal();
  });

//-----------------------------FUNCIONES DEL MODAL-----------------------------------------

// Obtén el modal y el botón de cerrar
var modal = document.querySelector('.modal');
var closeBtn = document.querySelector('.close');

// Añade un evento click al botón de cerrar para cerrar el modal
closeBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

// Añade un evento click a cualquier parte del modal para cerrarlo también
modal.addEventListener('click', function(event) {
  if (event.target === modal) {
      modal.style.display = 'none';
  }
});

// Función para abrir el modal
function openModal() {
  modal.style.display = 'block';
}
//------------------------------ACTUALIZAR-------------------------------------
function alert(){
  if (idusu == ""|| cece == "" || name =="" || telef == ""|| 
  especialidad == ""|| user ==""|| contra == ""|| pass=="") {
    swal("Hay campos vacios!", "Por favor llene todos los campos", "error");
  } else {
    const idusu = document.getElementById('idusu').value;
    const cece=  document.getElementById('cece').value;
    const name = document.getElementById('nombre').value;
    const telef = document.getElementById('telefono').value;
    const especialidad = document.getElementById('cargo').value;
    const user = document.getElementById('usuario').value;
    const contra = document.getElementById('contrasena').value;    
    const  pass = document.getElementById('pass').value;
    
    console.log(idusu, name, telef, especialidad, user, contra)
    axios.post('actualizarpersonal', {
      id: idusu,
      full_name: name,
      telefono: telef,
      Email: user,        
      especialidad: especialidad,
      cedula: cece,
      password: contra
  }, {
      headers: {
      'Content-Type': 'multipart/form-data'
  
      }
  }
  ).then((res) => {
      console.log(res.data)
  })
  .catch((err) => {
      console.log(err);
  })
  swal("Muchas gracias!", "Datos actualizados con exito!", "success");
  } 

}

//--------------------------------ELIMINAR------------------------------------------------
function eliminarper(btn) {
  var cedula = $(btn).closest('.div-table-row').find('.div-table-cell:nth-child(2)').text(); // Obtenemos el div de la fila
  console.log(cedula + "jsjjsjsj")  
  axios.delete('eliminarpersonal',{
      data:{
        cedula: cedula 
      }
      
    })
    .then(function (response) {
      var fila = $(btn).closest('.div-table-row');
      fila.remove();
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  }

//----------------------------------BUSCAR---------------------------------------