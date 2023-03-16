def valida():
    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3:
        try:
            opcion = int(input("¿Qué prefieres hacer? \n   1. Escribir una letra \n   2. Escribir una palabra \n   3. Salir del juego\nEscribe 1, 2 o 3: "))
        except ValueError:
            print("\n")
    return opcion
        
def intro_letra(lista_adivinada, lista_secreta, letras_usadas):
    letra = input("Introduce la letra a adivinar: ").upper()
    while letra in letras_usadas:
        print("Ya has introducido esa letra")
        letra = input("Introduce la letra a adivinar: ").upper()
    print(chr(27) + "[2J") #Limpiamos la pantalla
    letras_usadas.append(letra)    
    coincidencias = lista_secreta.count(letra)
    if coincidencias == 0: 
        print("No hay coincidencias con la letra " + letra + "\n")
    else:
        for index, value in enumerate(lista_secreta):
            if value == letra:
                lista_adivinada[index] = letra
    return lista_adivinada, letras_usadas


def game(lista_secreta, contador):
    lista_adivinada = ["_"]*len(lista_secreta)
    intento_palabra = ""
    print(chr(27) + "[2J") #Limpiamos la pantalla
    letras_usadas = []
    indicador_intento_palabra = 0
    while lista_adivinada != lista_secreta and intento_palabra != lista_secreta and contador>0: 
        """Mientras la lista adivinada no sea igual a la lista secreta y el contador sea mayor que 0, se sigue jugando""" 
        if indicador_intento_palabra == 1:
            print("Esta no es la palabra correcta")
            indicador_intento_palabra = 0
        print(lista_adivinada) 
        print("\nTe quedan " + str(contador) + " intentos\n")
        opcion = valida()
        if opcion == 1:
            lista_adivinada, letras_usadas = intro_letra(lista_adivinada, lista_secreta, letras_usadas)
        elif opcion == 2:
            palabra = input("\nIntroduce la palabra a adivinar: ").upper()
            intento_palabra = list(palabra)
            indicador_intento_palabra = 1
        elif opcion == 3:
            print("\nHasta la próxima\n")
            exit()
        contador -= 1
    if lista_adivinada != lista_secreta and intento_palabra != lista_secreta :
        resultado = "Perdiste"
    elif lista_adivinada == lista_secreta or intento_palabra == lista_secreta:
        resultado = "\nYou win!!!"
    return resultado, lista_adivinada, lista_secreta, intento_palabra

def main():
    palabra_secreta = input('Dime una palabra para adivinar: ').upper()
    lista_secreta = list(palabra_secreta) 
    lista_adivinada = ["_"]*len(lista_secreta) #Creamos una lista con tantos guiones como letras tenga la palabra secreta
    contador = 12
    resultado, lista_adivinada, lista_secreta, intento_palabra = game(lista_secreta, contador)
    print(resultado)
    if lista_adivinada == lista_secreta or intento_palabra == lista_secreta:
        print(lista_secreta)
    else:
        print("You tryed: ")
        print(lista_adivinada)
        print("The answer is:")
        print(lista_secreta)
        print("\n")
    inicial = 0
    menu(inicial)

def menu(inicial=1):
    if inicial == 1:
        print("Bienvenido al juego del ahorcado\n")
        eleccion = input("¿Quieres jugar? (S/N): ").upper()
    elif inicial == 0:
        eleccion = input("\n¿Quieres volver a jugar? (S/N): ").upper()
    else:
        print("Ha habido un error")

    if eleccion == "S":
        print("\n")
        main()
    elif eleccion == "N":
        print("\nHasta la próxima\n")
