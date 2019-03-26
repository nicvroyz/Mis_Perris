SeleccionaRegion();
function ValidarRut(rut){
        
    // Despejar Puntos
    var valor = rut.value.replace('.','');
    // Despejar Guión
    valor = valor.replace('-','');

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0,-1);
    dv = valor.slice(-1).toUpperCase();

    // Formatear RUN
    rut.value = cuerpo + '-'+ dv

    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if(cuerpo.length < 7) { alert("RUT Incompleto"); return false;}

    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;

    // Para cada dígito del Cuerpo
    for(i=1;i<=cuerpo.length;i++) {

        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);
        
        // Sumar al Contador General
        suma = suma + index;
        
        // Consolidar Múltiplo dentro del rango [2,7]
        if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

    }

    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);

    // Casos Especiales (0 y K)
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;

          // Validar que el cuerpo coincide con el dv
        if(dvEsperado != dv){
            console.log("Rut NO VALIDO");
            alert("El rut ingresado no es válido.");
            return false;
        }

        console.log("Rut VALIDO");
        
        return true;      
}

function SeleccionaRegion(){

    region = document.getElementById('select_region');    
    
    region.addEventListener("change", function(){
        console.log(region.value);
    });
}

function VerificarPassword(){
    pass = document.getElementById('password');
    pass_v = document.getElementById('password_verification');
    console.log(pass.value + " - " + pass_v.value)
    if(pass.value == pass_v.value){
        console.log('Password coincide')
        MostrarMensajeError(true);
        return true;
    }
    console.log('Password distintos');
    MostrarMensajeError(false);
    return false;
}

function MostrarMensajeError(correcto){
    console.log(correcto)
    if(correcto){
        $("#alert_message").fadeOut(1000, 0).slideUp(500, function(){
            $(this).remove();
        })
    }else{
        $("#alert_message").removeAttr('hidden');
        $("#alert_message").fadeIn(1000, 0);
    }
    
}



