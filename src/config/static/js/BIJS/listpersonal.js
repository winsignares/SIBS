function listcategory() {
    axios.get('/conlistpersonal', {
            responseType: 'json'
        })
        .then(function(res) {
            /*console.log(res['id']);*/
            let crear = "<div>#</div><div>DUI</div><div>Apellidos</div><div>Nombres</div><div>Teléfono</div><div>Cargo</div><div>Actualizar</div><div>Eliminar</div>"
            for (const x of datos) {
                let fila = "<div>"
                fila += x.DUI;
                fila += "</div>"


                fila += "<div>"
                fila += x.Nombre;
                fila += "</div>"

                fila += "<div>"
                fila += x.Telefono;
                fila += "</div>"

                fila += "<div>"
                fila += x.Cargo;
                fila += "</div>"

                fila += "</div>"
                crear += fila;

            }
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}