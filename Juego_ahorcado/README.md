<p align="center">
  <h1 align="center">Juego del Ahorcado</h3>
</p>
<p align="center">
<img src="https://www.toponimos.es/toponimos/img/ahorcado_0.png" width="220" height="220">
</p>


![Version](https://img.shields.io/badge/Version%20-1.0-0101DF.svg)
[![windows](https://img.shields.io/badge/Windows%20-compatible-1df31a.svg)](https://www.microsoft.com/es-es/windows) 


## About

Esta es una primera versión del tradicional juego del Ahorcado realizada en Python.
Se trata de una versión realizada como ejercicio de clase para el módulo Python Básico del Máster Big Data y Data Science 2022-2023 impartido por la Universidad Complutense de Madrid


## 1 - Descripción

En el juego participan 2 participantes. El jugador 1 introduce una palabra que al pulsar "intro" se convierte en secreta. El jugador 2 es el protagonista del juego en esta ronda,
y debe adivinar la palabra en un máximo de 12 intentos. En cada intento puede elegir entre dos opciones: 
- Introducir una letra para comprobar si está incluida en la palabra. 
- Introducir una palabra para comprobar si es la palabra correcta.

Si el jugador 2 consigue acertar antes de que se acaben los 12 intentos, éste gana y el jugador 1 pierde.
Por el contrario, si no consigue adivinar la palabra, éste pierde y el jugador 1 gana.

Tras esto, se invierten los roles, y comienza una nueva ronda.


## 2 - Diseño

### 2.1 - Panel de bienvenida

Al iniciar el juego nos aparecerá un panel inicial que nos da la bienvenida y nos pide confirmación de si queremos jugar, en caso de responder "n" se despide y se cierra el juego. 

### 2.2 - Palabra secreta

Cuando confirmamos que queremos jugar, nos pide que introduzcamos la palabra secreta. La introducimos y pulsamos "intro".
Esta fase corresponde al jugador 1.

### 2.3 - Panel de juego

A partir de aquí empieza la acción del jugador 2.
En la pantalla se generan tantos huecos como letras tenga la palabra secreta. 
Se muestra en numero de intentos.
Y nos pide elegir entre: 
   1. Escribir una letra
   2. Escribir una palabra
   3. Salir del juego

Escribimos 1, 2 o 3 para elegir una opción y verificar. 

Podemos escribir las letras y palabras tanto en mayusculas como en minusculas, y en caso de repetir una letra, el programa nos avisa y no nos descuenta ningún intento.

## 3 - Tecnologías, librerías y compatibilidad

Para jugar a esta versión del ahorcado tan solo es necesario tener instalado python en el ordenador.
No se requiere de ninguna librería adicional.

## 4 - A jugar!

Para jugar, abrimos la terminal desde la carpeta principal y ejecutamos el siguiente comando:

```cmd
python main.py
```
