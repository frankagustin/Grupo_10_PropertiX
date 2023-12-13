
const URL = "http://127.0.0.1:4000"
//const URL = "https://isidrobenitez.pythonanywhere.com"

const documento = document.getElementById('formulario');

documento.addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(documento); // Obtener los datos del formulario

    //formData.append('imagen', documento.imagen.files[0]); // Agregar la imagen al formulario

    fetch(URL + '/metodos', { // Enviar los datos al servidor
        method: 'POST', // Metodo de envio
        body: formData // Los datos del formulario
    })
     .then(res => res.json()) // Convertir la respuesta a JSON
     .then(data => { // Mostrar los datos en consola
        console.log(data);
        alert('Cliente agregado correctamente');
        window.location.href = '/clientes' // Redireccionar a index.html
    })

})