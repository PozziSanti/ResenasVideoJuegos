<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', function() {
  // Elementos del DOM
  const uname = document.getElementById('uname');
  const correo = document.getElementById('correo');
=======

document.addEventListener('DOMContentLoaded', function() {
  // Elementos del DOM
  const uname = document.getElementById('uname');
>>>>>>> f54580744e78aadc23587f0b3eab58dd16805092
  const pass1 = document.getElementById('password1');
  const pass2 = document.getElementById('password2');
  const btnContainer = document.querySelector('.btn-container');
  const btn = document.getElementById('login-btn');
  const form = document.querySelector('form');
  const msg = document.querySelector('.msg');
  const eye = document.querySelectorAll('.password-toggle')[0];
  const eye1 = document.querySelectorAll('.password-toggle')[1];
<<<<<<< HEAD
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 
=======

>>>>>>> f54580744e78aadc23587f0b3eab58dd16805092
  // Estados iniciales
  btn.disabled = true;
  const positions = ['shift-left', 'shift-top', 'shift-right', 'shift-bottom'];

  // Función para mover el botón
<<<<<<< HEAD

  function shiftButton() {
    const isEmpty = (uname.value.trim() === '' || pass1.value.trim() === '' || pass2.value.trim() === '' || correo.value.trim() === '');
 
    if (isEmpty) {
        showMsg();
        const currentPosition = positions.find(pos => btn.classList.contains(pos));
        let nextIndex = 0;
        
        if (currentPosition) {
            nextIndex = (positions.indexOf(currentPosition) + 1) % positions.length;
            btn.classList.remove(currentPosition);
        }
        
        btn.classList.add(positions[nextIndex]);
    } else {

        btn.classList.remove('shift-left', 'shift-top', 'shift-right', 'shift-bottom');
        btn.classList.add('no-shift');
    }
  } 

  // Función para mostrar mensajes
  function showMsg() {
    const isEmpty = (uname.value.trim() === '' || pass1.value.trim() === '' || pass2.value.trim() === '' || correo.value.trim() === '');
    const contrasCoinciden = (pass1.value.trim() === pass2.value.trim());
    const esEmailValido = emailRegex.test(correo.value.trim());

=======
  function shiftButton() {
    showMsg();
    const currentPosition = positions.find(pos => btn.classList.contains(pos));
    let nextIndex = 0;
    
    if (currentPosition) {
      nextIndex = (positions.indexOf(currentPosition) + 1) % positions.length;
      btn.classList.remove(currentPosition);
    }
    
    btn.classList.add(positions[nextIndex]);
  }

  // Función para mostrar mensajes
  function showMsg() {
    const isEmpty = uname.value.trim() === '' || pass.value.trim() === '';
>>>>>>> f54580744e78aadc23587f0b3eab58dd16805092
    btn.classList.toggle('no-shift', !isEmpty);

    if (isEmpty) {
      btn.disabled = true;
      msg.style.color = 'rgb(218, 49, 49)';
      msg.textContent = 'Rellena todos los campos';
<<<<<<< HEAD
    } else if (!esEmailValido) {
      btn.disabled = true;
      msg.style.color = 'rgb(218, 49, 49)';
      msg.textContent = 'El correo electrónico no es válido';
    } else if (!contrasCoinciden) { 
      btn.disabled = true;
      msg.style.color = 'rgb(218, 49, 49)';
      msg.textContent = 'Las contraseñas no coinciden';
    } else {
      // Si todas las validaciones pasan
      msg.textContent = 'Perfecto, puedes iniciar sesión';
      msg.style.color = '#92ff92';
      btn.disabled = false; // <-- El botón se habilita aquí
=======
    } else {
      msg.textContent = 'Perfecto, puedes iniciar sesión';
      msg.style.color = '#92ff92';
      btn.disabled = false;
>>>>>>> f54580744e78aadc23587f0b3eab58dd16805092
      btn.classList.add('no-shift');
    }
  }

  // Función de validación del formulario
<<<<<<< HEAD
=======
  function validarFormulario() {
    if (uname.value.trim() === '' || pass.value.trim() === '') {
      showMsg();
      return false;
    }
    return true;
  }
>>>>>>> f54580744e78aadc23587f0b3eab58dd16805092

  // Event Listeners
  btnContainer.addEventListener('mouseover', shiftButton);
  btn.addEventListener('mouseover', shiftButton);
  form.addEventListener('input', showMsg);
  btn.addEventListener('touchstart', shiftButton);

  // Toggle para mostrar/ocultar contraseña
  eye.addEventListener('click', function() {
    this.classList.toggle('fa-eye-slash');
    this.classList.toggle('fa-eye');
    pass1.type = (pass1.type === 'password') ? 'text' : 'password';
  },);

  eye1.addEventListener('click', function() {
    this.classList.toggle('fa-eye-slash');
    this.classList.toggle('fa-eye');
    pass2.type = (pass2.type === 'password') ? 'text' : 'password';
  });
});