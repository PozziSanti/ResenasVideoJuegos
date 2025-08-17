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

2. Instala las dependencias necesarias:

   ```bash
   npm install
   
4. Configura las variables de entorno según sea necesario (por ejemplo, base de datos, claves de API).
5. Inicia el servidor de desarrollo:

   ```bash
   npm start

## Uso
Una vez que la aplicación esté en funcionamiento, puedes acceder a las siguientes funcionalidades:

- **Inicio de sesión:** Utiliza las cuentas de prueba mencionadas anteriormente para acceder al sistema.

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

## Tecnologías Utilizadas
- Python 3
- HTML & CSS
- JavaScript
- Tailwind
