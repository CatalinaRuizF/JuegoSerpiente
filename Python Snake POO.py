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

#Clase de la ventana
class Screen():


    def __init__(self, ancho, alto, titulo, fondo, juego):
        self.ventana = turtle.Screen()
        self.ventana.title(titulo)
        self.ventana.bgcolor(fondo)
        self.ventana.setup(width = ancho, height = alto)
        self.ventana.tracer(0)

        #Configuro boton de cerrar
        canvas = self.ventana.getcanvas()
        root = canvas.winfo_toplevel()
        def on_close():
            juego.running = False
        root.protocol("WM_DELETE_WINDOW", on_close)

    #Metodo para el espacio de juego
    def setArena(self, lado, colorBorde, cuadricula=False):
        self.lado = lado
        self.colorBorde=colorBorde

        #Configuración de la Cuadricula si se desea mostrar, por defecto es False
        if cuadricula:
            ver = turtle.Turtle()
            ver.speed(0)
            ver.hideturtle()
            ver.goto(-(self.lado/2)-10,-(self.lado/2)-10)
            ver.color("white")
            ver.left(90)
            for i in range(10):
                ver.forward(self.lado)
                ver.right(90)
                ver.forward(20)
                ver.right(90)
                ver.forward(self.lado)
                ver.left(90)
                ver.forward(20)
                ver.left(90)

            hor = turtle.Turtle()
            hor.speed(0)
            hor.hideturtle()
            hor.goto(-(self.lado/2)-10,-(self.lado/2)-10)
            hor.color("white")
            for i in range(10):
                hor.forward(self.lado)
                hor.left(90)
                hor.forward(20)
                hor.left(90)
                hor.forward(self.lado)
                hor.right(90)
                hor.forward(20)
                hor.right(90)

        arena = turtle.Turtle()
        arena.speed(0)
        arena.hideturtle()
        arena.goto(-(self.lado/2)-10,-(self.lado/2)-10)
        arena.color(colorBorde)
        for i in range(4):
            arena.forward(self.lado)
            arena.left(90)
        self.ventana.update()
    

#Clase de la serpiente
class Serpiente():
    #Atributo de lista de los segmentos del snake
    segmentos = []

    def __init__(self, colorCabeza, colorSegmento):
        self.cabeza = turtle.Turtle()
        self.cabeza.speed(0)
        self.cabeza.shape("square")
        self.cabeza.color(colorCabeza)
        self.cabeza.penup()
        self.cabeza.goto(0,0)
        self.cabeza.direction = "stop"

        # Color de los segmentos
        self.colorSegmento = colorSegmento
    
    #Configuración de controles y creación de listener para la ventana
    def controles(self, ventana, arriba, abajo, izquierda, derecha):
        ventana.listen()
        ventana.onkeypress(self.arriba, arriba)
        ventana.onkeypress(self.abajo, abajo)
        ventana.onkeypress(self.izquierda, izquierda)
        ventana.onkeypress(self.derecha, derecha)

    #Métodos de dirección
    def arriba(self):
        if self.cabeza.direction != "down":
            self.cabeza.direction = "up"
    def abajo(self):
        if self.cabeza.direction != "up":
            self.cabeza.direction = "down"
    def izquierda(self):
        if self.cabeza.direction != "right":
            self.cabeza.direction = "left"
    def derecha(self):
        if self.cabeza.direction != "left":
            self.cabeza.direction = "right"

    # Método principal de movimiento
    def movimiento(self, juego, screen):
        
        if self.cabeza.direction == "up":
            y = self.cabeza.ycor()
            if y < ((screen.lado/2)-20):
                self.cabeza.sety(y + 20)
            else:
                juego.perder = True

        if self.cabeza.direction == "down":
            y = self.cabeza.ycor()
            if y > -(screen.lado/2):
                self.cabeza.sety(y - 20)
            else:
                juego.perder = True

        if self.cabeza.direction == "left":
            x = self.cabeza.xcor()
            if x > -(screen.lado/2):
                self.cabeza.setx(x - 20)
            else:
                juego.perder = True
        if self.cabeza.direction == "right":
            x = self.cabeza.xcor()
            if x<((screen.lado/2)-20):
                self.cabeza.setx(x + 20)
            else:
                juego.perder = True
    
    # Método para agregar segmentos
    def agregarSegmentos(self):
        self.nuevo_segmento = turtle.Turtle()
        self.nuevo_segmento.speed(0)
        self.nuevo_segmento.shape("square")
        self.nuevo_segmento.color(self.colorSegmento)
        self.nuevo_segmento.penup()
        self.segmentos.append(self.nuevo_segmento)

    # Método para mover el resto del cuerpo
    def moverCuerpo(self):
        tamanio = len(self.segmentos)
        for i in range(tamanio -1, 0, -1):
            x = self.segmentos[i - 1].xcor()
            y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(x,y)
        
        if tamanio > 0:
            x = self.cabeza.xcor()
            y = self.cabeza.ycor()
            self.segmentos[0].goto(x,y)

    # Comprueba si la serpiente colisiona consigo misma
    def colision(self, juego):
        for seg in self.segmentos:
            if seg.distance(self.cabeza) < 20:
                juego.alPerder(self)

# Clase de la comida
class Comida():

    def __init__(self, colorComida, screen):
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape("circle")
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



#-----------------------------------------MAIN-----------------------------------------#
# Instancia de Game
juego = Game(0.2)
juego.puntaje("white")

# Instancia de Screen
ventana = Screen(600,600,"Snake", "black", juego)
ventana.setArena(400,"red",False)

# Instancia de Serpiente
snake = Serpiente("white","gray")
snake.controles(ventana.ventana,"Up","Down", "Left", "Right")

# Instancia de comida
comida = Comida("red",ventana)

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
