"""Programa de juego de Trivia sobre Python
Integrantes: 
    Ana Karen Prieto
    Johana González
    Sofia Sachetti
"""
import random 
# Necesitamos pedir al usuario nombre y edad

nombre = input("Ingresa tu nombre: ").title()
edad = int(input("Ingresa tu edad: "))

#Función para obtener las preguntas con sus opciones y respuesta correcta
def obtener_preguntas():
    pregunta_1 = ("¿Es Python un programa de lenguaje de alto nivel?",("A) True","B) False"),"A")
    pregunta_2 = ("¿Quién es el creador de Python?",("A) Dennis Ritchie","B) James Gosling","C) Guido van Rossum"),"C")
    pregunta_3 = ("¿Cómo se comenta una línea en Python?",("A) //", "B) #", "C) /*"),"B")
    pregunta_4= ("¿Cómo se declara una función?",("A) func", "B) define", "C) def"),"C")
        
    preguntas = [pregunta_1,pregunta_2,pregunta_3,pregunta_4]
    return preguntas

#Función para obtener una respuesta por el usuario      
def obtener_respuesta(num_opciones):
    letras_opciones = ["A","B","C"]
    opciones = ""
    for l in range(num_opciones):
        opciones += letras_opciones[l] + ","
    letra = validar_respuesta(input(f"\n Tu respuesta ({opciones.rstrip(opciones[-1])}): ").strip().upper())
    return letra

#Función para validar que la respuesta sea una letra    
def validar_respuesta(letra):
    if letra.isalpha() and len(letra) == 1:
        return letra
    else:
        print("Solo se permite una letra.")
        return  validar_respuesta(obtener_respuesta())

#Función para obtener el número de opciones de la pregunta
def obtener_numero_opciones_pregunta(opciones):
    return len(opciones)

#Función para mostrar las opciones de la pregunta
def mostrar_opciones_pregunta(pregunta):
    for opcion in pregunta:
        print(f"\n {opcion}")
        
#Variables globales
respuestas_correctas = 0 
respuestas_incorrectas = 0

#Función que determina la funcionalidad del juego 
def juego_trivia():
    indice = 0
    intentos_max = 3 
    preguntas = obtener_preguntas()
    random.shuffle(preguntas)
    while indice < len(preguntas):   
        
        global respuestas_correctas
        global respuestas_incorrectas 
                
        pregunta, opciones, respuesta_correcta = preguntas[indice] 
        print(f"\n Pregunta {indice + 1} - {pregunta}")
        mostrar_opciones_pregunta(opciones)
        num_opciones =obtener_numero_opciones_pregunta(opciones)  
        respuesta = obtener_respuesta(num_opciones)    
        
        if respuesta == respuesta_correcta:
            respuestas_correctas += 1
        else:
            intentos_max -= 1
            respuestas_incorrectas += 1
                
        if intentos_max == 0:
            print("Haz fallado 3 veces. El juego a terminado.\n")
            break 
        indice += 1

# Determinar si el usuario es mayor de edad para jugar y comienza el juego

if (edad < 18):
    print("Lo sentimos, debes ser mayor de edad para jugar.")
else:
    # Mensaje de bienvenida al juego
    print(f"¡Bienvenido {nombre} a la trivia de Python! \nAntes de empezar el juego te contamos un poco su funcionamiento."
        "\nTe enviaremos preguntas y tu debes elegir la respuesta correcta." 
        "\nSi aciertas a la respuesta correcta ganas un punto."
        "\nSi la respuesta es incorrecta no sumas ningún punto, pere recuerda que no puedes fallas más de tres veces."
        "\nVamos a comenzar con las preguntas.")
    #Iniciamos el juego llamando a la funcion              
    juego_trivia()

#Muestra el puntaje de las respuestas correctas
print(f"{nombre} tu puntuación final es: {respuestas_correctas}/{len(obtener_preguntas())}.\n")

#Mensajes de despidida según su respuestas correctas
if respuestas_correctas == len(obtener_preguntas()):
    print("¡Excelente! Has respondido correctamente todas las preguntas.")
elif respuestas_correctas >= len(obtener_preguntas()) // 2:
    print("¡Buen trabajo! Sabes bastante sobre Python, pero aún puedes mejorar.")
else:
    print("Parece que necesitas repasar más sobre Python.")

print("Gracias por ingresar al Juego de la Trivia de Python.\n")