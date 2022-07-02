from termcolor import cprint, colored
from quiz.funciones import obtener_preguntas, preguntar, quiz, validar

valida = False
cprint('\nBienvenido/a!!!\n', 'green', attrs=['bold', 'blink'])

print("Ingrese la cantidad de preguntas a responder [entre 1 y 10]: ", end='')

while not valida:
    total_preguntas = input()
    valida = validar(total_preguntas)
    
    if not valida:
        print(colored('Lo siento, el valor no es válido', 'red'), 'vuelva a intentarlo: ', end='')

if __name__ == "__main__":
    quiz(int(total_preguntas))