# Proyecto Python
## ***QUIZ***
El poyecto se encuentra encapsulado dentro de un *entorno virtual*. Para poder iniciar este se debe estar dentro de la carpeta *venv* y ejecutar el comando _Scripts\activate_

Teniendo el entorno virtual activo se debe recuperar las dependencias para que el programa funcione como es esperado, para ello se ejecuta el comando _pip install -r requirements.txt_

Para correr el quiz se debe ejecutar de la siguiente manera:
~~~
    python -m quiz
~~~

Cuando ejecute el programa le solicitará ingresar la cantidad de preguntas que quiera responder, estas tienen que ser entre 1 y 10

Cada pregunta tiene al menos 4 alternativas y usted puede ingresar una respuesta correcta, aunque hay algunas preguntas que tienen más de una respuesta correcta usted solo necesita ingresar una de estas para que considere como Respuesta Correcta.

Al terminar con las preguntas le indicara el resultado de su intento, se la cantidad de preguntas respondidas correctamente es mayor al 50% se mostrará un mensaje de  _¡¡¡Felicitaciones!!!_ y si es menor un _Lástima_.
