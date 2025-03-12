window.addEventListener('load', ()=> {
    console.log('page loaded');
    const form = document.querySelector('#formulario');
    const usuario = document.querySelector('#usuario');
    const email = document.querySelector('#email');
    const contraseña = document.querySelector('#contraseña');
    const confirmarcontraseña = document.querySelector('#confirmarcontraseña');

    form.addEventListener('submit', (e)=>{
        e.preventDefault();

        if(validacionForm()){
            form.submit();
        }
    })
    
});

const validacionForm = () => {
    const usuarioValue = usuario.value.trim();
    const emailValue = email.value.trim();
    const contraseñaValue = contraseña.value.trim();
    const confirmarcontraseñaValue = confirmarcontraseña.value.trim();

    let isValid = true;
    if(!usuarioValue){
        console.log("Campo Vacio");
        fail(usuario,"Nombre vacio");
        isValid = false;
    }

    const err = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    if(!emailValue){
        fail(email, 'Correo vacio');
        isValid = false;
    }

    const er = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/
    if(!contraseñaValue){
        fail(contraseña, 'Contraseña vacia');
        isValid = false;
    }else if(contraseñaValue.length < 8){
        fail(contraseña, 'La contraseña debe tener minimo 8 caracteres')
    }else if(!contraseñaValue.match(er)){
        fail(contraseña, 'La contraseña debe contener al menos 1 mayuscula, 1 miniscula, y un numero')
    }

    if(!confirmarcontraseñaValue){
        fail(confirmarcontraseña, 'Por favor confirma la contraseña')
        isValid = false;
    }else if(contraseñaValue !== confirmarcontraseñaValue){
        fail(confirmarcontraseña, 'Las contraseñas no coinciden')
    }

    return isValid;

}

const fail =(input, msg) =>{
    const form = input.parentElement;
    const notif = form.querySelector('p');
    notif.innerText = msg;
    form.className = 'form-fail';               
}
