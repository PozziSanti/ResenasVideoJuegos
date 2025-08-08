const uname = document.querySelector('#uname');
const btnContainer = document.querySelector('.btn-container');
const btn = document.querySelector('#login-btn');
const form = document.querySelector('form');
const msg = document.querySelector('.msg');
btn.disabled = true;

function allFieldsFilled() {
    return uname.value !== '' && pass1.value !== '' && pass2.value !== '';
}

function shiftButton() {
    showMsg();
    const positions = ['shift-left', 'shift-top', 'shift-right', 'shift-bottom'];
    const currentPosition = positions.find(dir => btn.classList.contains(dir));
    const nextPosition = positions[(positions.indexOf(currentPosition) + 1) % positions.length];
    btn.classList.remove(currentPosition);
    btn.classList.add(nextPosition);
}


function showMsg() {
    const isEmpty = !allFieldsFilled();
    btn.classList.toggle('no-shift', !isEmpty);

    if (isEmpty) {
        btn.disabled = true;
        msg.style.color = 'rgb(218 49 49)';
        msg.innerText = 'Rellena todos los campos';
    } else {
        btn.disabled = false;
        msg.innerText = 'Perfecto, puedes registrarte';
        msg.style.color = '#92ff92';
        btn.classList.add('no-shift');
    }
}

//boton se mueve
btnContainer.addEventListener('mouseover', shiftButton);
btn.addEventListener('mouseover', shiftButton);
form.addEventListener('input', showMsg)
btn.addEventListener('touchstart', shiftButton);

const eye = document.querySelectorAll('.far')[0];
const eye2 = document.querySelectorAll('.far')[1];
const pass1 = document.querySelector('#password1');
const pass2 = document.querySelector('#password2');

function toggle1() {
    eye.classList.toggle('fa-eye-slash');
    eye.classList.toggle('fa-eye');
    pass1.type = (pass1.type === 'password') ? 'text' : 'password';
}
eye.addEventListener('click', toggle1); 


function toggle2() {
    eye2.classList.toggle('fa-eye-slash');
    eye2.classList.toggle('fa-eye');
    pass2.type = (pass2.type === 'password') ? 'text' : 'password';
}
eye2.addEventListener('click', toggle2); 


