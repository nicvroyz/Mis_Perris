let dbPromise = idb.open('mascotas-db', 1, (upgradeDb)=>{
    upgradeDb.createObjectStore('mascotas', {keyPath: 'pk'});
});

fetch('http://127.0.0.1:8000/getdata')
    .then((response) =>{
        return response.json();
    }).then((jsondata)=>{
        dbPromise.then((db)=>{
            let tx = db.transaction('mascotas', 'readwrite');
            let mascotasStore = tx.objectStore('mascotas');
            for(let key in jsondata){
                if(jsondata.hasOwnProperty(key)){
                    mascotasStore.put(jsondata[key]);
                }
            }
            
        });        
    });

let infoMascota = "Actualmente no hay datos almacenados en su sistema.";
let cantidadMascotas = 0;
dbPromise.then((db)=>{
    let tx = db.transaction('mascotas', 'readonly');
    let mascotasStore = tx.objectStore('mascotas');
    return mascotasStore.openCursor();
}).then(function lgoItems(cursor){
    if(!cursor){
        document.getElementById('offlineInfo').innerHTML = infoMascota;
        return;
    }
    for(let field in cursor.value){
        if(field == 'fields'){
            mascotaData = cursor.value[field];            
            cantidadMascotas++;
        }
    }
    let titulo = '<h2 class="text-center">Actualmente, contamos con ' + cantidadMascotas + ' perritos listos para adoptar.</h2>';
    let subTitle = '<h3 class="text-center">Por favor, vuelva a la aplicación cuando tenga conexión.</h3>';
    let icon = '<h4 class="text-center"><i class="fa fa-paw" style="font-size: 40px;"></i></h4>'
    infoMascota = titulo + '<br>' + subTitle + '<br>' + icon + '<br>';
        
    return cursor.continue().then(lgoItems);
});

if(window.navigator.onLine){
    document.getElementById('offlineInfo').style.display = 'none';
}else{
    document.getElementById('offlineInfo').style.display = 'block';
}