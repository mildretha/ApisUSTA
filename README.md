# ApisUSTA

Repositorio para las actividades del curso de APIs.

## Semana 1

- Instalación de Python 3.11.9
- Configuración de entorno virtual (venv)
- Creación de repositorio Git
- Script con type hinting y decoradores

## Ejecutar

_python main.py_

## Origen de datos
Encuesta anual de empresas: ejercicio 2024 (provisional) – CSV


# instalar Python 3.11.9 (si no estaba instalado)
python --version

# crear entorno virtual
python -m venv apis

# activar entorno virtual
conda activate apis
# o
source apis/bin/activate

# instalar librerías iniciales
pip install pandas rich

# inicializar repositorio
git init

# agregar archivos
git add .

# primer commit
git commit -m "Semana 1 - Configuración del proyecto y script inicial"

# conectar con repositorio remoto
git remote add origin https://github.com/mildretha/ApisUSTA.git

# subir cambios
git push -u origin main



## Semana 2 – Fundamentos de APIs y Validación de Datos

Durante esta semana se estudiaron los conceptos básicos necesarios para el desarrollo de APIs en Python. Se revisó el funcionamiento del protocolo HTTP, incluyendo los principales verbos (GET, POST, PUT y DELETE), los códigos de estado más comunes y el uso de headers para el intercambio de información entre cliente y servidor. También se analizaron los formatos de intercambio de datos, destacando JSON como estándar para APIs debido a su interoperabilidad y facilidad de lectura, en contraste con Pickle, que es un formato específico de Python.

Como parte práctica, se implementó un ejercicio de “API manual” que simula el flujo básico de una solicitud. El proceso consiste en recibir un string en formato JSON, parsearlo a un diccionario de Python, validar su estructura utilizando modelos de datos y finalmente generar una respuesta estructurada. Para la validación de datos se utilizó la librería Pydantic, creando esquemas de entrada (InputSchema) y salida (OutputSchema) asociados al dataset seleccionado en la fase anterior del proyecto.

Adicionalmente, se implementó la gestión de dependencias del proyecto mediante el archivo requirements.txt, donde se registran las principales librerías utilizadas como pandas, rich y pydantic. Esto permite garantizar la reproducibilidad del entorno de desarrollo y facilita la instalación de las dependencias necesarias para ejecutar el proyecto.


# instalar librería de validación
pip install pydantic

# generar archivo de dependencias
pip freeze > requirements.txt

# ejecutar script principal
python main.py

# subir cambios
git add .
git commit -m "Semana 2 - Implementación de validación con Pydantic"
git push



## Semana 3  Servidor Web y WSGI FLASK

Un servidor web permite que aplicaciones respondan a solicitudes HTTP de los clientes. En Python, Flask funciona mediante WSGI (Web Server Gateway Interface), que es una interfaz estándar entre el servidor web y las aplicaciones Python.

Routing

El routing permite definir qué función se ejecuta cuando un usuario accede a una URL específica. Cada endpoint se asocia a un verbo HTTP como GET, POST, PUT o DELETE.

Flask vs frameworks modernos

Flask es un microframework, ligero y flexible. Frameworks modernos como FastAPI incluyen validación automática, asincronía y documentación automática.

Síncrono vs Asíncrono

Síncrono: las solicitudes se procesan una por una.

Asíncrono: permite manejar múltiples solicitudes simultáneamente.

Flask funciona principalmente de forma síncrona.


# instalar Flask
pip install flask

# ejecutar servidor Flask
python app.py

# probar endpoints con curl
curl http://127.0.0.1:5000/status

curl -X POST http://127.0.0.1:5000/clean \
-H "Content-Type: application/json" \
-d '[{"nombre":"Ana","edad":25},{"nombre":"Ana","edad":25}]'

# subir cambios
git add .
git commit -m "Semana 3 - API básica con Flask"
git push


## Semana 4  FASTAPI


En esta semana se migró la API desarrollada previamente en Flask hacia FastAPI, un framework moderno para la construcción de APIs en Python basado en ASGI, lo que permite manejar múltiples solicitudes de forma más eficiente que el modelo tradicional WSGI. Durante la actividad se comprendió cómo el type hinting de Python funciona como fuente de verdad para la validación de datos, permitiendo que FastAPI genere automáticamente documentación interactiva mediante Swagger UI y Redoc. También se revisó de forma conceptual el uso de async/await para aplicaciones concurrentes. Como resultado de aprendizaje, se implementó una API funcional que reutiliza las funciones de limpieza de datos desarrolladas con Pandas, permitiendo ejecutar el servidor con Uvicorn y probar los endpoints directamente desde la documentación automática generada por FastAPI.

Comandos utilizados>

# instalar FastAPI y servidor ASGI
pip install fastapi uvicorn

# ejecutar API con uvicorn
uvicorn app_fastapi:app --reload

# acceder a documentación automática
http://127.0.0.1:8000/docs

# subir cambios
git add .
git commit -m "Semana 4 - Migración a FastAPI y documentación automática"
git push



