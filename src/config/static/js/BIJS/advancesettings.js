//Eliminar libros
function Eliminarlibro() {
    Swal.fire({
        icon: 'warning',
        html:
            'ingrese el id que desea eliminar' +
            '<input id="id_instructor" class="swal2-input">',
<<<<<<< HEAD

=======
>>>>>>> e04952e63f4a64c44b7aac550974f1269fdcb57b
    })

}

//Eliminar aprendiz
function EliminarEstudiantes() {
    Swal.fire({
<<<<<<< HEAD
        icon: 'warning',
        title: 'Eliminar Estudiantes',
        html:
        '<input id="EliminarAprendiz" class="swal2-input" placeholder="Escribe aqui el id del usuario">',
      showCancelButton: true,
      confirmButtonText: 'Enviar',
      cancelButtonText: 'Cancelar',
        
    }).then((result) => {
        if (result.isConfirmed) {
          const eliminarAprendiz = document.getElementById('EliminarAprendiz');
          axios.get('api/eliminar_Users', {
            
            id: eliminarAprendiz.value
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

          
      }}  
      )};
      
=======
        title: 'Eliminar Estudiantes',
        html:
            '<input id="EliminarAprendiz" class="swal2-input" placeholder="Escribe tu consulta aquí">',
        showCancelButton: true,
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
    }).then((result) => {
        if (result.isConfirmed) {
            const EliminarAprendiz = document.getElementById('EliminarAprendiz').value;

            
            // Aquí puedes consumir el API utilizando la consulta
        }
    });


};
>>>>>>> e04952e63f4a64c44b7aac550974f1269fdcb57b


//Eliminar Instructor
function EliminarDocente() {
    Swal.fire({
        title: 'Eliminar Instructor',
        input: 'select',
        icon: 'warning',
        showCancelButton: true,
        inputOptions: {
            'Rol': {
                Roles: 'Elige',
                Instructor: 'Instructor'
            },
        },
        html:
            'ingrese el id que desea eliminar' +
            '<input id="id_instructor" class="swal2-input">',
    })
};
// funcion eliminar bitacora
function EliminarBitacora() {
    Swal.fire({
        title: 'desea eliminar la bitacora',
        text: 'al momento de borrarse los datos no podran recuperarse',
        confirmButtonText: 'confirmar',
        showCancelButton: true,
        icon: 'warning'

    })
};

function EliminarPadministrativo() {
    Swal.fire({
        title: 'Eliminar Personal Administrativo',
        input: 'select',
        icon: 'warning',
        showCancelButton: true,
        inputOptions: {
            'Rol': {
                Roles: 'Elige',
                Personal_Administrativo: 'Personal Administrativo'
            },
        },
        html:
            'ingrese el id que desea eliminar' +
            '<input id="id_instructor" class="swal2-input">',
    })
}