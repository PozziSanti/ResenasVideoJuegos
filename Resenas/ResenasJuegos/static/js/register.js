
document.addEventListener('DOMContentLoaded', function() {
  // Elementos del DOM
  const uname = document.getElementById('uname');
  const pass1 = document.getElementById('password1');
  const pass2 = document.getElementById('password2');
  const btnContainer = document.querySelector('.btn-container');
  const btn = document.getElementById('login-btn');
  const form = document.querySelector('form');
  const msg = document.querySelector('.msg');
  const eye = document.querySelectorAll('.password-toggle')[0];
  const eye1 = document.querySelectorAll('.password-toggle')[1];

  // Estados iniciales
  btn.disabled = true;
  const positions = ['shift-left', 'shift-top', 'shift-right', 'shift-bottom'];

  // Función para mover el botón
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
    btn.classList.toggle('no-shift', !isEmpty);

    if (isEmpty) {
      btn.disabled = true;
      msg.style.color = 'rgb(218, 49, 49)';
      msg.textContent = 'Rellena todos los campos';
    } else {
      msg.textContent = 'Perfecto, puedes iniciar sesión';
      msg.style.color = '#92ff92';
      btn.disabled = false;
      btn.classList.add('no-shift');
    }
  }

  // Función de validación del formulario
  function validarFormulario() {
    if (uname.value.trim() === '' || pass.value.trim() === '') {
      showMsg();
      return false;
    }
    return true;
  }

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