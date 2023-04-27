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
                        <div id= "${i}" class="div-table-cell" style="width: 15%;">${datos[index].dui}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].nombre}</div>
                        <div class="div-table-cell" style="width: 12%;">${datos[index].telefono}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos[index].cargo}</div>
                        <div class="div-table-cell" style="width: 9%;">
                                <a onclick="openModal()" class="btn btn-success"><i class="zmdi zmdi-refresh"></i></a>
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
 
  window.addEventListener('load', function() {
    viewpersonal();
  });
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

  function actuperson() {
    
    const idusu = document.getElementsByName('idusu').value;
    const name = document.getElementsByName('nombre').value;
    const telef = document.getElementsByName('telefono').value;
    const especialidad = document.getElementsByName('cargo').value;
    const user = document.getElementsByName('usuario').value;
    const contra = document.getElementsByName('contrasena').value;    
    const  pass = document.getElementsByName('pass').value;

    

// Función para abrir el modal

function alert(){
Swal.fire({
    position: 'top',
    icon: 'success',
    title: 'Tus datos han sido  guardados con exito',
    showConfirmButton: false,
    timer: 1500
  })
}
    axios.post('actualizarpersonal', {
        id: idusu,
        full_name: name,
        telefono: telef,
        Email: user,        
        especialidad: especialidad,
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