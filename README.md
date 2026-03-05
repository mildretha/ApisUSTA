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

## Semana 2 – Fundamentos de APIs y Validación de Datos

Durante esta semana se estudiaron los conceptos básicos necesarios para el desarrollo de APIs en Python. Se revisó el funcionamiento del protocolo HTTP, incluyendo los principales verbos (GET, POST, PUT y DELETE), los códigos de estado más comunes y el uso de headers para el intercambio de información entre cliente y servidor. También se analizaron los formatos de intercambio de datos, destacando JSON como estándar para APIs debido a su interoperabilidad y facilidad de lectura, en contraste con Pickle, que es un formato específico de Python.

Como parte práctica, se implementó un ejercicio de “API manual” que simula el flujo básico de una solicitud. El proceso consiste en recibir un string en formato JSON, parsearlo a un diccionario de Python, validar su estructura utilizando modelos de datos y finalmente generar una respuesta estructurada. Para la validación de datos se utilizó la librería Pydantic, creando esquemas de entrada (InputSchema) y salida (OutputSchema) asociados al dataset seleccionado en la fase anterior del proyecto.

Adicionalmente, se implementó la gestión de dependencias del proyecto mediante el archivo requirements.txt, donde se registran las principales librerías utilizadas como pandas, rich y pydantic. Esto permite garantizar la reproducibilidad del entorno de desarrollo y facilita la instalación de las dependencias necesarias para ejecutar el proyecto.


## Semana 3  Servidor Web y WSGI

Un servidor web permite que aplicaciones respondan a solicitudes HTTP de los clientes. En Python, Flask funciona mediante WSGI (Web Server Gateway Interface), que es una interfaz estándar entre el servidor web y las aplicaciones Python.

Routing

El routing permite definir qué función se ejecuta cuando un usuario accede a una URL específica. Cada endpoint se asocia a un verbo HTTP como GET, POST, PUT o DELETE.

Flask vs frameworks modernos

Flask es un microframework, ligero y flexible. Frameworks modernos como FastAPI incluyen validación automática, asincronía y documentación automática.

Síncrono vs Asíncrono

Síncrono: las solicitudes se procesan una por una.

Asíncrono: permite manejar múltiples solicitudes simultáneamente.

Flask funciona principalmente de forma síncrona.


