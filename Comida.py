import turtle
import time
import random

# Clase de la comida
class Comida():

    def __init__(self, colorComida, screen):
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape('img/Comida.gif')
        self.comida.color(colorComida)
        self.comida.penup()
        self.comida.goto(0,40)

        self.lado = screen.lado
    
    # Método de cuando la serpiente colisiona con la comida
    def alColisionar(self, serpiente, game):
        if serpiente.cabeza.distance(self.comida) < 20:
            condicion = True
            while condicion:
                # Posición random
                x = (random.randint(0, 19)*20)-(self.lado/2)
                y = (random.randint(0, 19)*20)-(self.lado/2)

                # Comprueba que no coincida con el cuerpo de la serpiente
                if len(serpiente.segmentos)>0:
                    for seg in serpiente.segmentos:
                        if x==seg.xcor() and y==seg.ycor():
                            condicion = True
                            break
                        else:
                            condicion = False
                else:
                    condicion = False
            # Mueve la comida a la nueva posición
            self.comida.goto(x,y)

            # Se suma el puntaje
            game.actualizarPuntaje(10)
            
            # Se le agrega un nuevo segmento a la sepiente
            serpiente.agregarSegmentos()

            return True
        else:
            return False     

