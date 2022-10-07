## Workspace MySQL Gitpod and Docker

### To install on Docker (Windows, Linux or Mac)

    $ docker-compose up -d

### Pasos para probar la aplicacion (backend)

Entrar en la carpeta api:

    $ cd api

Una vez alli debemos activar el entorno virtual e instalar las dependencias

    $ pipenv shell && pipenv install

Habilitar el comando flask

    $ export FLASK_APP=src/app.py

Verificar que exista la base de datos agenda si no existe crearla

    CREATE DATABASE agenda;

Ejecutar las migraciones en la base de datos

    $ flask db upgrade


### Pasos para probar la aplicacion (frontend)

Entrar en la carpeta app:

    $ cd app

Una vez alli debemos instalar todos las dependencias

    $ npm install

Ejecutar la aplicacion:

    $ npm start