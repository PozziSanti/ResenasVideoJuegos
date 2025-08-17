# Hit or Quit 👾

## 📌 Acerca del proyecto

Hit or Quit es una plataforma colaborativa donde los usuarios pueden compartir y consultar reseñas de videojuegos. El objetivo es crear una comunidad activa que aporte valor a través de opiniones honestas y detalladas sobre diversos títulos. El proyecto está desarrollado utilizando tecnologías web modernas y busca ser una herramienta útil tanto para jugadores como para desarrolladores.

## 🗂️ Estructura

- **ResenasVideoJuegos/**  
  - `manage.py`  
  - `requirements.txt`  
  - `README.md`  
  - `db.sqlite3`  
  - **resenas/** (App principal de reseñas)  
    - **migrations/**  
    - **templates/resenas/**  
    - **static/**  
    - `admin.py`  
    - `apps.py`  
    - `models.py`  
    - `views.py`  
    - `urls.py`  
  - **users/** (App de usuarios y autenticación)  
    - **migrations/**  
    - **templates/users/**  
    - **static/**  
    - `admin.py`  
    - `apps.py`  
    - `models.py`  
    - `views.py`  
    - `urls.py`  
  - **staticfiles/** (Archivos estáticos compilados)  
  - **templates/** (Plantillas base globales)

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

### Funcionalidades principales

- **Registro e inicio de sesión**  
  Los usuarios pueden registrarse o iniciar sesión con las cuentas de prueba indicadas en este README.

- **Explorar reseñas**  
  Cualquier usuario puede navegar por las reseñas de videojuegos publicadas.

- **Crear y gestionar reseñas**  
  Los usuarios logueados pueden:
  - Publicar nuevas reseñas sobre videojuegos.
  - Editar o eliminar sus propias reseñas.

- **Panel de administrador**  
  Accesible en `http://127.0.0.1:8000/admin/` con una cuenta de superusuario o la cuenta de prueba de administrador.  
  Desde aquí se pueden gestionar usuarios, reseñas y permisos.

## Cuentas de prueba

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

## 📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más información.
