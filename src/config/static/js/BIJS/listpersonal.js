function listpersonal(){

    axios.get('/conlistpersonal',{
        
        responseType: 'json'
    })
    .then(function(res){
        /*console.log(res['id']);*/
        console.log(res)
        let nose = function(res){
        let crear = "<div>DUI</div><div>Nombre completo</div><div>Teléfono</div><div>Cargo</div>"
        for (const x of res) {
            let fila = "<div><div>"
            fila += x.Dui;
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
            console.log(crear);
        }        
    };
    nose(res);
    })
    .catch(function(err){
        console.log(err);
    })
    .then(function(){
    });
}

function lgf(){
    console.log("dbgtrnyrnyr")
}