from termcolor import cprint
from quiz.funciones import obtener_preguntas, preguntar

total_preguntas = 5

def quiz():
    cprint('Bienvenido/a!!!\n', 'green', 'on_yellow', attrs=['bold'])
    
    preguntas = obtener_preguntas(total_preguntas)
    cant_correctas = 0
    
    for num, pregunta in enumerate(preguntas, 1):
        print(f'Pregunta N° {num}:')
        cant_correctas += preguntar(pregunta)
    
    color = ''
    mensaje = ''
    plural = ''
    
    if cant_correctas > 1:
        plural = 's'
        
    if cant_correctas / num >= 0.5:
        color = 'green'
        mensaje = 'Felicitaciones'
    else:
        color = 'red'
        mensaje = 'Lastima'
        
    cprint(f"{mensaje}, obtuviste {cant_correctas} respuesta{plural} correcta{plural} de un total de {num} preguntas.", color)

if __name__ == "__main__":
    quiz()