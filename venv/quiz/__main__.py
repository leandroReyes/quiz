from quiz.funciones import obtener_preguntas, preguntar

total_preguntas = 5

def quiz():
    print("Bienvenido/a!!!\n")
    
    preguntas = obtener_preguntas(total_preguntas)
    cant_correctas = 0
    
    for num, pregunta in enumerate(preguntas, 1):
        print(f'Pregunta N° {num}:')
        cant_correctas += preguntar(pregunta)
        
    print(f"Obtuviste {cant_correctas} correctas de un total de {num} preguntas")

if __name__ == "__main__":
    quiz()