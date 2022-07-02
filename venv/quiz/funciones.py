from string import ascii_lowercase
import json
import random
from termcolor import colored

def obtener_preguntas(total_preguntas):
    with open('quiz\pokemon.json', encoding='utf-8') as fh:
        preguntas = json.load(fh)["preguntas"]
        return random.sample(preguntas, total_preguntas)

def preguntar(pregunta):
    respuestas_correctas = pregunta["respuestas"]

    alternativas = pregunta["respuestas"] + pregunta["alternativas"]

    alternativas_mezcladas = random.sample(alternativas, len(alternativas))

    respuesta = obtener_respuesta(
        pregunta["pregunta"], 
        alternativas_mezcladas
    )

    if respuesta in respuestas_correctas:
        print(colored('¡¡¡Respuesta Correcta!!!', 'green'))
        return 1
    else:
        print(colored("Respuesta Incorrecta: la respuesta correcta es", 'red'), colored(f"{' o '.join(respuestas_correctas)}", 'blue'))
        return 0
        
def obtener_respuesta(pregunta, alternativas):
    print(f'{pregunta}')
    alternativas_ordenadas = dict(zip(ascii_lowercase, alternativas))
    
    for letra, alternativa in alternativas_ordenadas.items():
        print(f'\t{letra}) {alternativa}')
        
    letra_respuesta = input('\nOpción: ')
    while letra_respuesta not in alternativas_ordenadas:
        print(f"Ingrese una opción valida, estas son {', '.join(alternativas_ordenadas)}")
        letra_respuesta = input('\nOpción: ')

    return alternativas_ordenadas[letra_respuesta]