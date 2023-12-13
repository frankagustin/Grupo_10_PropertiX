document.addEventListener("DOMContentLoaded",function(){
    //fetch("https://restcountries.eu/rest/v2/")
/*     const apiUrl =  "https://jsonplaceholder.typicode.com/photos";
   // const apiUrl =  "https://restcountries.eu/rest/v2/"

    fetch(apiUrl).then(response => response.json)
     .then(users => console.log(users))
       // datadecode(users)
       // );  // funcion asincronica de javascript que permite hacer peticiones

   // const result = document.getElementById("resultado");

});

*/
    fetch("https://api.escuelajs.co/api/v1/products")
    .then(response => response.json()
    )
    .then(dataDecode=>descodificar(dataDecode)
    )

})
/* fetch a la API Platzi Fake Store API
url: https://api.escuelajs.co/docs#/files/FilesController_seeUploadedFile

*/

let descodificar = (datos) => {
   /* let cadena="";*/
    for(i=0;i<=datos.length - 1;i++){
        /*cadena="ID: "+datos[i].id+ ". Titulo: "+ datos[i].title + ". Descripcion: " + datos[i].description +" ";
       document.getElementById("tabla").innerHTML += "<ul><li>"+cadena+ "<img src="+datos[i].images+" width='200'></img></li></ul><br>";*/
        document.getElementById("tabla").innerHTML += "<td>"+datos[i].id+ "</td><td>"+datos[i].title+"</td><td>"+datos[i].description+"</td><td><img src="+datos[i].images+" width='200'></img></td";
        /* if(i==50){
            break;
        }  */

    };
}


/* datos.forEach(element => {
        cadena="ID: "+element.id+ "Nombre: "+ element.title;
       // console.log(cadena)
       document.getElementById("resultado").innerHTML += cadena;
       
       
    }); */
    //console.log(cadena)
    //document.getElementById("resultado").innerHTML = cadena;
let buscar = document.getElementById("btnBuscar");
/*
function busca(){
    let serchQuery = document.getElementById("buscar").value.trim();
    document.getElementById("resultado").innerHTML=""
    console.log(serchQuery)
    let apiUrl = "https://api.escuelajs.co/api/v1/products/?title=" + serchQuery

    fetch(apiUrl)
    .then(response => response.json()
    )
    .then(dataDecode=>descodificar(dataDecode)
    )
} */
buscar.addEventListener("click",()=>{
    let serchQuery = document.getElementById("buscar").value.trim();
    document.getElementById("tabla").innerHTML=""
    console.log(serchQuery)
    let apiUrl = "https://api.escuelajs.co/api/v1/products/?title=" + serchQuery

    fetch(apiUrl)
    .then(response => response.json()
    )
    .then(dataDecode=>descodificar(dataDecode)
    )

}) 