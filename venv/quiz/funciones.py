from string import ascii_lowercase
import json
import random
from termcolor import colored


def validar(total_preguntas):
    try:
        total_preguntas = int(total_preguntas)
    except ValueError:
        return False #si la conversión falla devolvemos False
    return total_preguntas in range(1, 11)

def quiz(total_preguntas):
    preguntas = obtener_preguntas(total_preguntas)
    cant_correctas = 0
    
    for num, pregunta in enumerate(preguntas, 1):
        print(f'\nPregunta N° {num}:')
        cant_correctas += preguntar(pregunta)
    
    color = ''
    mensaje = ''
    plural = ''
    
    if cant_correctas > 1:
        plural = 's'
        
    if cant_correctas / num >= 0.5:
        color = 'green'
        mensaje = '¡¡¡Felicitaciones!!!'
    else:
        color = 'red'
        mensaje = 'Lástima'
        
    print(colored(f"{mensaje}", color, attrs=['bold', 'underline']) + f", obtuviste", colored(f"{cant_correctas}", 'magenta'), f"respuesta{plural} correcta{plural} de un total de", colored(f"{num}", 'magenta'), f"preguntas.")

def obtener_preguntas(total_preguntas):
    with open('quiz\pokemon.json', encoding='utf-8') as archivo:
        preguntas = json.load(archivo)["preguntas"]
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
        print(colored("Respuesta Incorrecta:", 'red'), f"la respuesta correcta es", colored(f"{' o '.join(respuestas_correctas)}", 'blue'))
        return 0
        
def obtener_respuesta(pregunta, alternativas):
    print(f'{pregunta}')
    alternativas_ordenadas = dict(zip(ascii_lowercase, alternativas))
    
    for letra, alternativa in alternativas_ordenadas.items():
        print(colored(f'\t{letra})', 'cyan'), f'{alternativa}')
        
    letra_respuesta = input('\nOpción: ')
    while letra_respuesta not in alternativas_ordenadas:
        print(colored(f"Opción ingresada no es válida.", 'yellow'),  f"Por favor ingrese una opción; estas son", colored(f"{', '.join(alternativas_ordenadas)}", 'cyan'))
        letra_respuesta = input('\nOpción: ')

    return alternativas_ordenadas[letra_respuesta]