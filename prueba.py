import requests

def trivia_fetch(number):
    trivia_fetch = requests.get(f"http://numbersapi.com/{number}?json")
    if trivia_fetch.status_code == 200:
       print("Suertudo, tu numero tiene suerte: " )
    
    #Acceder al valor clave text en el json 
    content = trivia_fetch.json()
    #print("Información de la trivia", content)
    #print("Mensaje de tu numero: ", content["text"])

    for k,v in content.items():
       return print("Tu número nos dice que: ", content), k,v

    
def main():
    number = input("Dame tu numero de la suerte: ")
    trivia_fetch(number)


if __name__=="__main__":
  main()
