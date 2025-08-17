# Hit or Quit 👾

## 📌 Acerca del proyecto

Hit or Quit es una plataforma colaborativa donde los usuarios pueden compartir y consultar reseñas de videojuegos. El objetivo es crear una comunidad activa que aporte valor a través de opiniones honestas y detalladas sobre diversos títulos. El proyecto está desarrollado utilizando tecnologías web modernas y busca ser una herramienta útil tanto para jugadores como para desarrolladores.

## 🗂️ Estructura

└── ResenasVideoJuegos
    ├── Resenas
    │   ├── ResenasJuegos
    │   │   ├── __pycache__
    │   │   ├── apps
    │   │   │   ├── comment
    │   │   │   ├── favorite
    │   │   │   ├── post
    │   │   │   └── user
    │   │   ├── blog
    │   │   │   ├── __pycache__
    │   │   │   └── configurations
    │   │   ├── media
    │   │   │   └── post
    │   │   ├── static
    │   │   │   ├── assets
    │   │   │   ├── css
    │   │   │   └── js
    │   │   ├── staticfiles
    │   │   │   ├── admin
    │   │   │   ├── assets
    │   │   │   ├── css
    │   │   │   ├── django-browser-reload
    │   │   │   └── js
    │   │   └── templates
    │   │       ├── category
    │   │       ├── components
    │   │       ├── layouts
    │   │       ├── pages
    │   │       ├── partials
    │   │       ├── post
    │   │       ├── registration
    │   │       └── user

## Instalación

Para poner en marcha el proyecto en tu entorno local, sigue los siguientes pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/PozziSanti/ResenasVideoJuegos.git
   cd ResenasVideoJuegos

2. Crea un entorno virtual:

   ```bash
   python -m venv env

3. Activa el entorno virtual (Windows):
   
   ```bash
   env\Scripts\activate
- En caso de tener Linux o Mac:

  ```bash
   source env/bin/activate
5. Instala las dependencias desde `requirements.txt`:
   
   ```bash
   pip install -r requirements.txt
   
7. Aplica migraciones:
   
   ```bash
   python manage.py migrate
   
9. Crea un superusuario (opcional, para acceder al panel de admin):
    
    ```bash
   python manage.py createsuperuser
    
11. Ejecuta el servidor:
    
    ```bash
     python manage.py runserver

## 🚀 Uso

Una vez que el servidor esté en funcionamiento (`python manage.py runserver`), accede a la aplicación en tu navegador en:

👉 `http://127.0.0.1:8000/`

### Funcionalidades principales

- **Registro e inicio de sesión**  
  Los usuarios pueden registrarse o iniciar sesión con las cuentas de prueba indicadas en este README.

- **Explorar reseñas**  
  Cualquier usuario puede navegar por los posts de videojuegos publicadas.

- **Crear y gestionar reseñas**  
  Los usuarios logueados pueden:
  - Guardar/Eliminar posts de sus favoritos.
  - Ver y hacer comentarios en posts.
  - Editar y eliminar sus propios comentarios.
 
  En caso de que ese usuario logueado sea promovido a admin podrá:
  - Crear posts y categorizarlos.
  - Editar y Eliminar sus propios posts.
  - Eliminar comentarios de sus propios posts.
  - Guardar/Eliminar posts de sus favoritos.
  - Hacer comentarios en posts.
  - Editar y eliminar sus propios comentarios.

- **Panel de administrador**  
  Accesible en `http://127.0.0.1:8000/admin/` con una cuenta de superusuario o la cuenta de prueba de administrador.  
  Desde aquí se pueden gestionar usuarios, reseñas y permisos.

## 🔑 Cuentas de prueba

Para facilitar la prueba de la aplicación sin necesidad de registrarse, se han creado cuentas de usuario predefinidas:

- **Usuario:** `testuser`
  - **Contraseña:** `testpass`
  - **Rol:** Usuario estándar

- **Usuario:** `adminuser`
  - **Contraseña:** `adminpass`
  - **Rol:** Administrador

Estas cuentas permiten acceder a las funcionalidades básicas y administrativas del sistema.

## 👥 Colaboradores

- **Pozzi Santiago** – *Fullstack Developer*
- **Prodanov Sofía** – *Frontend Developer*
- **Suarez Fernando** – *Backend Developer*
- **Gnus Matías** – *Backend Developer*

## ⚙️ Tecnologías Utilizadas
- Python 3
- HTML & CSS
- JavaScript
- Tailwind CSS

## 📄 LicenciaEste proyecto está bajo la **Licencia MIT**.  
Puedes consultar el texto completo de la licencia en el archivo [LICENSE](LICENSE).
