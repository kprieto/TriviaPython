"""Programa de juego de Trivia sobre Python
Integrantes: 
    Ana Karen Prieto
    Johana González
    Sofia Sachetti
""" 

# Necesitamos pedir al usuario nombre y edad

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Determinar si el usuario es mayor de edad para jugar y comenzar el juego

if (edad < 18):
    print("Lo sentimos, debes ser mayor de edad para jugar.")
else:
    # Mensaje de bienvenida al juego
    print(f"¡Bienvenido {nombre} a la trivia de Python! \nAntes de empezar el juego te contamos un poco su funcionamiento. 
        \nTe enviaremos preguntas y tu debes elegir la respuesta correcta. 
        \nSi aciertas a la respuesta correcta ganas un punto.
        \nSi la respuesta es incorrecta no sumas ningún punto, pere recuerda que no puedes fallas más de tres veces.
        \nVamos a comenzar con las preguntas.
        ")
    #Iniciamos el juego llamando a la funcion
    
    preguntas = (("¿Es Python un programa de lenguaje de alto nivel?", 
        ("A) True", 
        "B) False"),
        "A"),
        
        ("¿Quién es el creador de Python?",
        ("A) Menty Pthon",
        "B) G"))
        
        )