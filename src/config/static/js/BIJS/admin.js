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
function mostrarAlerta() {
    Swal.fire({
      title: '¿Estás seguro?',
      text: '¡No podrás revertir esta acción!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí, eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.value) {
        // Si el usuario hace clic en el botón "Sí", se llama a la función GuardarAdministrador
        GuardarAdministrador();
      }
    })
  }