### ¿Que es una API?

API: Application Programming Interface
Interfaz de Programación de  Aplicaciones.

Intermediario que me ayuda a comunicarme entre un programa A y un programa B 

-> Conjunto de reglas y protocolos para comunicación entre aplicaciones.
->  Permite exponer datos y funcionalidades de forma segura. 
-> Actúa como una capa conectora o un "mesero" que toma tu pedido (solicitud) y te trae lo que ordenaste (respuesta), sin que necesites saber cómo funciona la cocina (el sistema interno). 

API como contrato y ejemplo practico

Una API abstrae la complejidad. No necesita saber como un sistema calcula un dato, solo necesitas saber c omo pedirlo. 

La documentación de una API funciona como un contrato: "Si me envías una solicitud con esta estructura especifica, yo me comprometo a responderte de esta manera. 

Ejemplo: 

Agencia de viajes online. 

Como sitios como Kayak y Expedia obtienen los precios de vuelos de cientos de aerolíneas casi al instante?

No acceden directamente a las bases de datos de las aerolíneas.  
En su lugar, utilizan la API de cada aerolínea. Envían una solicitud ("Vuelo de Bogotá a Medellín, 25 de diciembre") y la API devuelve los resultados ("Vuelo AV123, 8:00 AM, $150.00)


Tipos populares: 

SOAP -> Protocolo Simple de Acceso a Objetos
Estricto y estandar
Utiliza formato XML para estructurar los datos 
Es mas rígido y verboso.

REST --> Transferencia de Estado Representacional. 

Conjunto de principios de arquitectura, no un protocolo estricto.
Generalmente Utiliza JSON.
Es mas ligero y facil de leer 
Una API que sigue estos principios se conoce como API RESTFUL, es el estilo mas popular. 

DEMO  - Acceder a una API con cURL
Usaremos la Numbers API para obtener datos curiosos sobre numeros. 

http://numbersapi.com/

formas adecuadas para dirigir a un servidor 

Get, Post, Put, Delete

Solicitar información --> GET 
Crear nuevo recurso   --> Post
Modificar recurso     --> Put
Eliminar un recurso   --> Delete

Json --> JavaScript Object Notation. 

El poder de Json esta en usarlo dentro de nuestras aplicaciones. 

Pasos para consumir una API en Código. 

    1.- importar una libreria para hacer peticiones http:
        request en python 
        httpclient en java 

    2.- Realizar la peticion Get a la URL de la API 

    3.- Recibir respuesta Json como una cadena de texto. 

    4.- Parsear o deserializar esa cadena para convertirla en un ojbeto o diccionario nativo. 

    5.- Acceder a los datos usando notacion de objetos o diccionarios. 

Objetivo de la evaluación 

Diseñar y construir una aplicación de línea de comandos que utilice una API pública para crear un cuestionario interactivo. 

Aplicar los conceptos de funciones de entrada/Salida, lógica condicional y consumo de APIs en un proyecto práctico. 

Practica: 

construye un cuestionario interactivo:

La lógica es simple: 
-> El programa le pide un numero al usuario 
-> Usa numbers API para obtener un dato curioso sobre ese numero
-> Muestra el dato curioso al usuario 
-> Puedes ser tan creativo como quieras con la interacción. 

Requisitos tecnicos

El programa debe incluir funcion especifico para que pueda ser calificada automaticamente: 

trivia_fetch(number)
debe existir en el programa

Debe recibir un numero como parametro 

Debe devolver un diccionario (dict)
con la trivia de ese numero obtenida de la API 

Investigar como convertir el JSON en un diccionario
Despues crear funciones adicionales para impriirlo en la linea de comandos.  

Preguntar al usuario un numero





