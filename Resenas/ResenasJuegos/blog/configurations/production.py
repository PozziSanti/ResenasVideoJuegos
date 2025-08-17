from .base import *

DEBUG=False

#TODO:CONFIGURAR DOMINIO AL HACER DEPLOY A PRODUCTION 
ALLOWED_HOSTS=["127.0.0.1","midominio-production.com"]

#TODO:CONFIGURAR DB PARA PRODUCTION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",

        # En caso de usar una postres utilizo:
        # "ENGINE": "django.db.backends.postgresql",

        # En caso de usar una postres utilizo:
        # "ENGINE": "django.db.backends.mysql",

        # "NAME": os.getenv('DB_NAME'),
        # "USER": os.getenv('DB_USER'),
        # "PASSWORD": os.getenv('DB_PASSWORD'),
        # "HOST": os.getenv('DB_HOST'),
        # "PORT": os.getenv('DB_PORT'),
    }
}

os.environ["DJANGO_PORT"]="8080"
