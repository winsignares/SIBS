function eliminarFila() {
    /*    const div = document.getElementById("hola");
        div.parentNode.removeChild(div);*/
    alert("algo")
    console.log("algo")
}

function EliminarEstudiantes() {
    /*const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: 'success',
        title: 'Signed in successfully'
    })*/
    tblestadosolicitud.ajax.reload(null, flase)
}