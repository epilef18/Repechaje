# Proyecto Python con PostgreSQL

Este proyecto está diseñado para ser ejecutado en un entorno de Python y utiliza PostgreSQL como base de datos. En este archivo `README.md` se explica cómo configurar y cargar los datos en la base de datos desde un archivo de volcado de PostgreSQL (`bodegas.sql`) generado con `pg_dump`.

## Requisitos

- Python 3.x
- PostgreSQL 12 o superior
- pip (para la gestión de dependencias de Python)
- Un entorno virtual (opcional, pero recomendado)

## Instrucciones

### 1. Descomprimir el archivo FELIPE_VILLARROEL.zip

### 2. Crear un entorno virtual

usar el comando: python -m venv env
activar el entorno virtual usando:  .\env\Scripts\activate

### 3. Instalar las dependencias

pip install -r requirements.txt

### 4. Configurar PostgreSQL

psql -U postgres

crear base de datos:  CREATE DATABASE nombre_de_base_de_datos;

### 5. Cargar el archivo SQL en la base de datos

usar el comando: psql -U postgres -d nombre_de_base_de_datos -f bodegas.sql

### 6. Configurar la conexion a la base de datos en Django

en el archivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_base_de_datos',
        'USER': 'postgres',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 7. Migrar la base de datos

python manage.py migrate

### 8. Ejecutar el proyecto Django

python manage.py runserver

Esto arrancará el servidor de desarrollo en http://127.0.0.1:8000/, donde podrás acceder a tu proyecto Django.


## Información pertinente:

### 1. Datos de los usuarios

user: fred
pass: chips1234

user: polulo
pass: tomisking

### 2. Dependencias

asgiref==3.8.1
Django==5.1.5
psycopg2==2.9.10
python-dotenv==1.0.1
sqlparse==0.5.3
tzdata==2025.1

### 3. Referente a los modelos

Se añadió una entidad extra, llamada Cotizaciones, para relacionar al usuario con las bodegas y generar el precio total de manera mas expedita

