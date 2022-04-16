import turtle
import time
import random

#Clase juego con funciones generales
class Game():

    perder = False
    running = True
    puntos = 0
    max_pun = 0

    def __init__(self, delay=0.2):
        self.delay = delay

    #Creación del texto de puntaje
    def puntaje(self, colorTexto):
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.color(colorTexto)
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(0,250)
        self.texto.write("Puntos: 0     Puntaje maximo: 0",
                        align = "center", font = ("times", 24, "normal"))

    #Actualización del puntaje
    def actualizarPuntaje(self, puntos):
        self.puntos +=puntos

        if self.puntos>self.max_pun:
            self.max_pun=self.puntos
        
        self.texto.clear()
        self.texto.write("Puntos: {}     Puntaje maximo: {}".format(self.puntos, self.max_pun),
                        align = "center", font = ("times", 24, "normal"))
    
    #Resetear Puntaje
    def resetearPuntaje(self):
        self.puntos = 0
        self.texto.clear()
        self.texto.color("white")
        self.texto.goto(0,250)
        self.texto.write("Puntos: {}     Puntaje maximo: {}".format(self.puntos, self.max_pun),
                        align = "center", font = ("times", 24, "normal"))
    
    #Texto de Game Over
    def gameOver(self):
        self.texto.clear()
        self.texto.color("red")
        self.texto.write("GAME OVER", align = "center", font = ("times", 40, "bold",))
        time.sleep(2)
    
    #Método que se ejecuta al perder
    def alPerder(self, serpiente):

        #Reseteo variable bandera
        self.perder = False

        #Lanzo texto de game over
        self.gameOver()

        #Reseteo la posición de la serpiente
        serpiente.cabeza.direction = "stop"
        serpiente.cabeza.goto(0,0)
        for seg in serpiente.segmentos:
            seg.hideturtle()
        serpiente.segmentos.clear()

        #Reseteo el puntaje
        self.resetearPuntaje()
