const URL = "http://127.0.0.1:4000"
//const URL = "https://isidrobenitez.pythonanywhere.com"

/* const queryString = window.location.search; // Obtener la query string de la URL
const urlParams = new URLSearchParams(queryString); // Obtener los parámetros de la query string

const id = urlParams.get('codigo'); // Obtener el id del cliente

fetch(URL + '/clientes/' + id) // Obtener el cliente
.then(res => res.json()) // Convertir la respuesta a JSON
.then(data => { // Mostrar los datos en consola
    console.log(data);
    document.getElementById('codigo').value = data.id;
    document.getElementById('nombre').value = data.nombre;
    document.getElementById('dni').value = data.dni;
    document.getElementById('direccion').value = data.direccion;
    document.getElementById('telefono').value = data.telefono;
}); */

const documento = document.getElementById('formulario');

documento.addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(documento); // Obtener los datos del formulario
    const id = document.getElementById('codigo').value
    fetch(URL + '/modificar/' + id, { // Enviar los datos al servidor
        method: 'PUT', // Metodo de envio
        body: formData // Los datos del formulario
    })
     .then(res => res.json()) // Convertir la respuesta a JSON
     .then(data => { // Mostrar los datos en consola
        console.log(data);
        alert('Cliente modificado correctamente');
        window.location.href = '/clientes'/*window.location.reload(); // Recargar la página*/
    })
})