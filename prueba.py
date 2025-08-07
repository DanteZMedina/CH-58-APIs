import requests


def trivia_fetch(number):
    trivia_fetch = requests.get(f"http://numbersapi.com/{number}?json")
    if trivia_fetch.status_code == 200:
       print("Suertudo, tu numero tiene suerte " )
       content = trivia_fetch.json()
       return content
    else:
        print("Lo siento, no se pudo obtener la trivia.")
        return {}   

#como puedo retornar un diccionario?
    
def main():
    number = input("Dame tu numero de la suerte: ")
    trivia_fetch(number)


if __name__=="__main__":
  main()
