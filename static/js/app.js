function validarDatos(){
    let numero1 = document.getElementById("txtNumero1");
    let numero2 = document.getElementById("txtNumero2");

    if (numero1.value=="" || numero2.value==""){
        return false;
    }else{
        return true;
    }
}

/**
 * Función para realizar la petición asincrona al servidor
 */
function sumar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url = "/sumar";
        fetch(url, {method: "POST",body: data})
        .then(respuesta => respuesta.json())
        .then(resultado =>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.resultado; 
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("Problemas","Faltan datos","warning")
    }
}

function restar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url = "/restar";
        fetch(url, {method: "POST",body: data})
        .then(respuesta => respuesta.json())
        .then(resultado =>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.resultado; 
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("Problemas","Faltan datos","warning")
    }
}

function multiplicar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url = "/multiplicar";
        fetch(url, {method: "POST",body: data})
        .then(respuesta => respuesta.json())
        .then(resultado =>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.resultado; 
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("Problemas","Faltan datos","warning")
    }
}

function dividir(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url = "/dividir";
        fetch(url, {method: "POST",body: data})
        .then(respuesta => respuesta.json())
        .then(resultado =>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.resultado; 
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("Problemas","Faltan datos","warning")
    }
}