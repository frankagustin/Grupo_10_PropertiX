const URL = "http://127.0.0.1:4000"
//const URL = "https://isidrobenitez.pythonanywhere.com"

//alert('ingreso a listado')
fetch(URL + '/metodos') // Obtener los Clientes
    .then(res => res.json()) // Convertir la respuesta a JSON
    .then(data => { // Mostrar los datos en consola
        let html = ''; // Variable para guardar el HTML
        console.log(data);

        data.forEach(element => {

        /*imagen='';

        //Bucktick `` para concatenar , interpolacion de variables ${}
        if (element.foto === null) {
            imagen = '';
        }
        else
        {
            imagen = `${element.foto}`; 
        } */

        html = html + `<tr>
            <td>${element.nombre}</td>
            <td>${element.dni}</td>
            <td>${element.direccion}</td>
            <td>${element.telefono}</td>
           
            <td><a href="/clientes/${element.id}"><button type="button" class="btn btn-warning">Modificar</button></a></td>
            <td><button type="button" class="btn btn-danger" onclick="eliminar(${element.id})">Eliminar</button></td>
        </tr>`;
       });

       document.getElementById('lista_personas').innerHTML = html;
    });


function eliminar(id){

    fetch(URL + '/metodos/' + id, { // Hago la petición a la API para eliminar el cliente
        method: 'DELETE' // Indico el método HTTP
    }).then(res => res.json()) // Convierto la respuesta a JSON
    .then(data => {
        console.log(data); // Muestro los datos en consola
        alert('Cliente eliminado: ' + id); // Muestro un mensaje al usuario
        window.location.reload(); // Recargo la página
    });


}