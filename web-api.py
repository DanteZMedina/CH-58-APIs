import requests


#Realizar una petición GET a la API de NumbersAPI
trivia_fetch = requests.get("http://numbersapi.com/42?json")

#Imprimir el código de estado de la respuesta, se espera 200
print("Código de respuesta: ", trivia_fetch.status_code)


# convertir el contenido de la respuesta a formato JSON
# y almacenarlo en una variable
trivia = trivia_fetch.json()
print("Información de la trivia", trivia)

# acceder al valor de la clave 'text' en el JSON
print("Mensaje de la trivia:", trivia['text'])
# acceder al valor de la clave 'number' en el JSON
print("Número de la trivia:", trivia['number'])

#fstring

