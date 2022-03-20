'''

nombre juego: snake by Esmeralda,Karen and Catalina (provicional)

1.reglas serpiente
    a)cuatro cuadros de longitud de la serpiente inicial de la serpiente
    b)si choca con obstaculos (paredes del laberinto) muere instantaneamente, aparece mensaje y aparece pantalla de inicio del juego
    c)Si come alimento de color equivocado disminuye una unidad de longitud
    d)Si come alimento de color correcto dado por pantalla aumenta una unidad de tamaño
    e)Si la serpiente se toca a si misma, muere instaneamente, aparece mensaje y aparece pantalla de inicio
    f)Si la serpiente tiene un cuadro de longitud y come alimento incorrecto, muere instantaneamente,aparece mensaje y aparece pantala de inicio
    g)si la serpiente no come la cantidad de comida pendida por pantalla en el tiempo establecido, acaba el juego, aparece mensaje y aparece pantalla de inicio 
    h)La serpiente aumenta de velocidad cada vez que come dos alimentos correctos

2.reglas puntos 
    a)Cuando come correcto gana +1 y eso suma al puntaje acumulable en pantalla
    b)Cuando come equivocado pierde -1 y se resta del puntaje acumulable en pantalla
    c)Rango de puntos(por definir)
    d)Cuando la serpiente muere en cualquiera de los niveles los puntos se reinician(comienza marcador en 0)
    e)
    f)

3.reglas comida
    a)la comida es un (por definir) de extencion (por definir)
    b)cuando la serpiente toca la comida incorrecta: la comida desaparece y resta puntos
    c)cuando la serpiente toca la comida correcta: la comida desaparece y suma puntos
    d)cuando la comida de color correcto desaparesca cambian todas las demas de color
    e)comida es inmovible (?)
    

4.reglas tiempo
    a)tiempo limite para que la serpiente coma la cantidad de comida es (por definir)
    b)
    c)
    d)

5.reglas enemigos: 
    1.1)definicion de enemigos:
        a)es un enemigo la comida que no puede consumir la serpiente
        b)es un enemigo los muros que no puede tocar
        c)en un enemigo la misma serpiente si se come a ella misma
        d)es un enemigo el tiempo si se acaba el limite del temporizador
    1.2)reglas:
        a)cuando serpiente come la comida equivocada: pierde
        b)cuando serpiente toca muro: pierde
        c)cuando serpiente no come la comida correcta antes de que acabe el tiempo limite del temporizador:pierde     

6.reglas nivel:
    1.1)definicion de niveles
        a)nivel 1:
        -****menor dificultad***
        -cantidad de comida(por definir)
        -posicion muros(por definir)
        -limite de tiempo(por definir)
        -puntaje inicia en 0
        -limite minimo de comida (por definir)
        -puntaje por puntos (provicional):
            6-6 = GANA
            3-6 = GANA
            2-6 = PIERDE
            0-6 = PIERDE

        b)nivel 2:
        -****dificultad media***
        -cantidad de comida(por definir)
        -posicion muros(por definir)
        -limite de tiempo(por definir)
        -puntaje inicia según el ultimo puntaje acumulado del nivel 1
        -limite minimo de comida (por definir)
        -puntaje por puntos (provicional):
            10-10 = GANA
            5-10 = GANA
            4-10 = PIERDE
            0-10 = PIERDE   

        c)nivel 3:
        -****mayor dificultad***
        -cantidad de comida(por definir)
        -posicion muros(por definir)
        -limite de tiempo(por definir)
        -puntaje inicia según el ultmo puntaje acumulado del nivel 2
        -limite minimo de comida (por definir)
        -puntaje por puntos (provicional):
            16-16 = GANA
            8-16 = GANA
            7-16 = PIERDE
            0-16 = PIERDE
    
    1.2)reglas:
        a)pasa nivel con determinada cantidad de puntos
        b)unicamente tres niveles de dificultad (+bonus(por definir))


DIMENCIONES DEL JUEGO

    1.1 Pantalla primaria:
        ancho:600
        alto:500
        color:(por definir)
    1.2 Elementos pantalla:
         A)pantalla de entrada al juego:
                a.1)cuadro de inicio
                a.2)fondo y nombre del juego
         B)pantalla de juego basica:
                b.1)cuadro de tiempo
                b.2)cuadro de alimento por comer
                b.3)cuadro que muestre el numero de nivel
                b.4)cuadro que muestre puntaje acumulado
                b.5)cuadro que muestre el numero de alimentos que falta por consumir para pasar de nivel

                    B.a)definicion de obstaculos(MUROS)
                        -Muros colocados en las posiciones de X nivel:
                        Muro1: 
                            alto:   ancho:
                        Muro2:
                            alto:   ancho:
                        Muro3: 
                            alto:   ancho:
                        Muro4:
                            alto:   ancho:
                        Muro5: 
                            alto:   ancho:
                        Muro6:
                            alto:   ancho:
                        Muro7: 
                            alto:   ancho:
                        Muro8:
                            alto:   ancho:
                    B.b)definicion de obstaculos(COMIDA)
                        -Posicion de los obstaculos de comida
                        (por definir)
        C)Pantalla de perdida:
            a)Mensaje por perdida del juego(por definir)
            b)fondo:por definir

        D)Pantalla de victoria                    
            a)Mensaje de victoria del juego:
                -aparece cuando se termina un nivel: ejm: pasaste al nivel 2
                -aparece cuando se termina todos los niveles: ejm: felicidades has completado el juego
                -aparece puntaje final acumulado
                -retorna a la pantalla de entrada al juego.                                                     










'''