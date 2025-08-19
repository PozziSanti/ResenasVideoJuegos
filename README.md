# Hit or Quit 👾

## 📌 Acerca del proyecto

Hit or Quit es una plataforma colaborativa donde los usuarios pueden compartir y consultar reseñas de videojuegos. El objetivo es crear una comunidad activa que aporte valor a través de opiniones honestas y detalladas sobre diversos títulos. El proyecto está desarrollado utilizando tecnologías web modernas y busca ser una herramienta útil tanto para jugadores como para desarrolladores.

## 🗂️ Estructura

```bash
┣ 📂env
┃ ┣ 📂Scripts
┃ ┃ ┣ 📜activate.bat
┃ ┃ ┣ 📜deactivate.bat
┃ ┃ ┗ ...
┃ ┗ ...
┣ 📂Resenas
┃ ┣ 📂ResenasJuegos
┃ ┃ ┣ 📂apps
┃ ┃ ┃ ┣ 📂comment
┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃ ┃ ┣ 📜tests.py
┃ ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃ ┣ 📂favorite
┃ ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃ ┃ ┣ 📜tests.py
┃ ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃ ┣ 📂post
┃ ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃ ┃ ┣ 📜tests.py
┃ ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃ ┗ 📂user
┃ ┃ ┃   ┣ 📂migrations
┃ ┃ ┃   ┣ 📜__init__.py
┃ ┃ ┃   ┣ 📜admin.py
┃ ┃ ┃   ┣ 📜apps.py
┃ ┃ ┃   ┣ 📜decorators.py
┃ ┃ ┃   ┣ 📜forms.py
┃ ┃ ┃   ┣ 📜models.py
┃ ┃ ┃   ┣ 📜signals.py
┃ ┃ ┃   ┣ 📜tests.py
┃ ┃ ┃   ┣ 📜urls.py
┃ ┃ ┃   ┗ 📜views.py
┃ ┃ ┣ 📂blog
┃ ┃ ┃ ┣ 📂configurations
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃ ┃ ┣ 📜local.py
┃ ┃ ┃ ┃ ┗ 📜production.py
┃ ┃ ┃ ┣ 📜asgi.py
┃ ┃ ┃ ┣ 📜settings.py
┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃ ┣ 📜views.py
┃ ┃ ┃ ┗ 📜wsgi.py
┃ ┃ ┣ 📂media
┃ ┃ ┃ ┗ 📂post
┃ ┃ ┃   ┣ 📂default
┃ ┃ ┃   ┃ ┗ 📜post_default.png
┃ ┃ ┃   ┗ 📂images
┃ ┃ ┣ 📂static
┃ ┃ ┃ ┣ 📂assets
┃ ┃ ┃ ┃ ┣ 📂about_us
┃ ┃ ┃ ┃ ┃ ┣ 📜profile_fer.png
┃ ┃ ┃ ┃ ┃ ┣ 📜profile_mati.png
┃ ┃ ┃ ┃ ┃ ┣ 📜profile_santi.png
┃ ┃ ┃ ┃ ┃ ┗ 📜profile_sofi.png
┃ ┃ ┃ ┃ ┣ 📂header_icons
┃ ┃ ┃ ┃ ┃ ┣ 📜buscador.png
┃ ┃ ┃ ┃ ┃ ┣ 📜favicon1.ico
┃ ┃ ┃ ┃ ┃ ┣ 📜hit_or_quit_logo.png
┃ ┃ ┃ ┃ ┃ ┗ 📜menu_hamburguesa.png
┃ ┃ ┃ ┃ ┗ 📂login_register
┃ ┃ ┃ ┃   ┗ 📜fondo.png
┃ ┃ ┃ ┣ 📂css
┃ ┃ ┃ ┃ ┣ 📜register.css
┃ ┃ ┃ ┃ ┗ 📜styles.css
┃ ┃ ┃ ┗ 📂js
┃ ┃ ┃   ┣ 📜header_logic.js
┃ ┃ ┃   ┣ 📜login.js
┃ ┃ ┃   ┣ 📜register.js
┃ ┃ ┃   ┣ 📜sidebar_logic.js
┃ ┃ ┃   ┗ 📜tailwind.js
┃ ┃ ┣ 📂staticfiles
┃ ┃ ┃ ┗ 📂admin
┃ ┃ ┃   ┣ 📂css
┃ ┃ ┃   ┣ 📂img
┃ ┃ ┃   ┗ 📂js
┃ ┃ ┣ 📂templates
┃ ┃ ┃ ┣ 📂category
┃ ┃ ┃ ┃ ┣ 📜category_create.html
┃ ┃ ┃ ┃ ┣ 📜category_delete.html
┃ ┃ ┃ ┃ ┣ 📜category_detail.html
┃ ┃ ┃ ┃ ┣ 📜category_list.html
┃ ┃ ┃ ┃ ┗ 📜category_update.html
┃ ┃ ┃ ┣ 📂components
┃ ┃ ┃ ┃ ┣ 📂cards
┃ ┃ ┃ ┃ ┃ ┗ 📜flip_card.html
┃ ┃ ┃ ┃ ┣ 📂commons
┃ ┃ ┃ ┃ ┃ ┣ 📜footer.html
┃ ┃ ┃ ┃ ┃ ┗ 📜header.html
┃ ┃ ┃ ┃ ┗ 📂ui
┃ ┃ ┃ ┃   ┗ 📜sidebar.html
┃ ┃ ┃ ┣ 📂layouts
┃ ┃ ┃ ┃ ┣ 📜auth_layout.html
┃ ┃ ┃ ┃ ┣ 📜base_layout.html
┃ ┃ ┃ ┃ ┗ 📜general_layout.html
┃ ┃ ┃ ┣ 📂pages
┃ ┃ ┃ ┃ ┣ 📜about.html
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜privacy.html
┃ ┃ ┃ ┃ ┗ 📜terms.html
┃ ┃ ┃ ┣ 📂partials
┃ ┃ ┃ ┃ ┣ 📂home_icons
┃ ┃ ┃ ┃ ┃ ┣ 📜add_icon.html
┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_left.html
┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_right.html
┃ ┃ ┃ ┃ ┃ ┣ 📜delete_icon.html
┃ ┃ ┃ ┃ ┃ ┣ 📜favorited_flag.html
┃ ┃ ┃ ┃ ┃ ┣ 📜sad_icon.html
┃ ┃ ┃ ┃ ┃ ┣ 📜unfavorited_flag.html
┃ ┃ ┃ ┃ ┃ ┗ 📜warning_icon.html
┃ ┃ ┃ ┃ ┣ 📂sidebar_icons
┃ ┃ ┃ ┃ ┃ ┣ 📜action.html
┃ ┃ ┃ ┃ ┃ ┣ 📜beauty.html
┃ ┃ ┃ ┃ ┃ ┣ 📜compass.html
┃ ┃ ┃ ┃ ┃ ┣ 📜ghost.html
┃ ┃ ┃ ┃ ┃ ┣ 📜home.html
┃ ┃ ┃ ┃ ┃ ┣ 📜motorcycle.html
┃ ┃ ┃ ┃ ┃ ┣ 📜multiplayer.html
┃ ┃ ┃ ┃ ┃ ┣ 📜perfil.html
┃ ┃ ┃ ┃ ┃ ┣ 📜puzzle.html
┃ ┃ ┃ ┃ ┃ ┣ 📜sports.html
┃ ┃ ┃ ┃ ┃ ┣ 📜stars.html
┃ ┃ ┃ ┃ ┃ ┗ 📜target.html
┃ ┃ ┃ ┃ ┗ 📜_sidebar_link.html
┃ ┃ ┃ ┣ 📂post
┃ ┃ ┃ ┃ ┣ 📜post_comment.html
┃ ┃ ┃ ┃ ┣ 📜post_create.html
┃ ┃ ┃ ┃ ┣ 📜post_delete_comment.html
┃ ┃ ┃ ┃ ┣ 📜post_delete.html
┃ ┃ ┃ ┃ ┣ 📜post_detail.html
┃ ┃ ┃ ┃ ┣ 📜post_list.html
┃ ┃ ┃ ┃ ┗ 📜post_update.html
┃ ┃ ┃ ┣ 📂registration
┃ ┃ ┃ ┃ ┣ 📜signin.html
┃ ┃ ┃ ┃ ┗ 📜signup.html
┃ ┃ ┃ ┗ 📂user
┃ ┃ ┃   ┣ 📜change_password.html
┃ ┃ ┃   ┣ 📜edit_profile.html
┃ ┃ ┃   ┗ 📜user_profile.html
┃ ┃ ┣ 📜db.sqlite3
┃ ┃ ┗ 📜manage.py
┃ ┣ 📜.env
┃ ┣ 📜.gitignore
┃ ┗ 📜requirements.txt
┣ 📜LICENSE
┗ 📜README.md
```  


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
   python manage.py makemigrations
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

- **Usuario:** `testingusercomun`
  - **Contraseña:** `facilito123`
  - **Rol:** Usuario estándar

- **Usuario:** `testinguserpan`
  - **Contraseña:** `facil123`
  - **Rol:** Administrador

Estas cuentas permiten acceder a las funcionalidades básicas y administrativas del sistema.

## 👥 Colaboradores

- **Pozzi Santiago** – *Fullstack Developer*
- **Prodanov Sofía** – *Frontend Developer*
- **Suarez Fernando** – *Backend Developer*
- **Gnus Matías** – *Backend Developer*

📌 Organización del Proyecto

El equipo utiliza Trello para la planificación y seguimiento de tareas:

👉 [![Trello Board](https://img.shields.io/badge/Trello-Proyecto%20Final-026AA7?logo=trello&logoColor=white)](https://trello.com/b/Fpkr5eiX/proyecto-final)

## ⚙️ Tecnologías Utilizadas
- Python 3
- HTML & CSS
- JavaScript
- Tailwind CSS

## 📄 LicenciaEste proyecto está bajo la **Licencia MIT**.  
Puedes consultar el texto completo de la licencia en el archivo [LICENSE](LICENSE).
