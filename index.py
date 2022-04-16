
#-----------------------------------------MAIN-----------------------------------------#
import turtle
import time
import random
import Game as g
import Screen as s
import Serpiente as ser
import Comida as c

# Instancia de Game
juego = g.Game(0.2)
juego.puntaje("white")

# Instancia de Screen
ventana = s.Screen(600,600,"Snake", "black", juego)
ventana.setArena(510,"green",False)

# Instancia de Serpiente
snake = ser.Serpiente("white","#834827")
snake.controles(ventana.ventana,"Up","Down", "Left", "Right")

# Instancia de comida
comida = c.Comida("blue",ventana)

# Loop Principal
while juego.running:
    # Actualizacuón de la ventana
    ventana.ventana.update()

    # Comprueba la bandera de perder
    if juego.perder:
        juego.alPerder(snake)

    # Comprueba si colisionó con la comida
    if comida.alColisionar(snake, juego):
        comida.alColisionar(snake, juego)
        snake.moverCuerpo()
        continue
    # Mueve el cuerpo de la serpiente
    snake.moverCuerpo()

    # Mueve la cabeza de la serpiente
    snake.movimiento(juego,ventana)

    # Comprueba si la serpiente colisionó consigo misma
    snake.colision(juego)

    # Delay para regular la velocidad de juego
    time.sleep(juego.delay)
