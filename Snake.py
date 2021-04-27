import turtle
import time
import random
import os

# Area de juego

ventana = turtle.Screen()
ventana.title(' Juguemos Snake ')
ventana.bgcolor('white')
ventana.setup(width = 700, height = 700)
ventana.tracer(0)								# Hace animaciones mas interactivas con el usuario

# Head

head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.penup()									# Con este método no deja rastro nuestro elemento
head.goto(0,0)
head.direction = 'stop'

# Food

food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.penup()
food.goto(100,0)
food.color('red')
food.direction = 'left'

# Body
body = []

#Marcador

score = 0
high_score = 0

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color('Black')
marcador.penup()
marcador.hideturtle()
marcador.goto(0,310)
marcador.write('Score:  0    Hight Score: 0 ', align="center", font = ("Arial", 20))

# Funciones

def arriba():
	head.direction = 'up'

def abajo():
	head.direction = 'down'

def derecha():
	head.direction = 'right'

def izquierda():
	head.direction = 'left'

def mov():
	if head.direction == 'up':
		y = head.ycor()
		head.sety (y + 20)

	if head.direction == 'down':
		y = head.ycor()
		head.sety (y - 20)

	if head.direction == 'right':
		x = head.xcor()
		head.setx (x + 20)

	if head.direction == 'left':
		x = head.xcor()
		head.setx (x - 20)



def dificultad(x):
	if len(body) > 2:
		return x - 0.05

def longitud(z):
	return len(z)


# Haciendo que las flechas dirijan 
ventana.listen()							# Esta funcion '.listen' permite que la ventana de trabajo capte las entradas del teclado, como un input'
ventana.onkeypress(arriba, 'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(derecha, 'Right')
ventana.onkeypress(izquierda, 'Left')

## Definir niveles

tiempo = 0.3


while True:
	ventana.update()

	# Colisiones bordes

	if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
		time.sleep(1)
		head.goto(0,0)
		head.direction = 'stop'

		for i in body:
			i.goto(900,900)

		body.clear()

		#Resetear marcador

		score = 0
		marcador.clear()
		marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Arial", 20))

	if head.distance(food) < 20:
		x = random.randint(-330, 300)
		y = random.randint(-330, 330)
		food.goto(x,y)


		new_body = turtle.Turtle()
		new_body.speed(0)
		new_body.shape('circle')
		new_body.color('black')									
		new_body.penup()
		body.append(new_body)

		score += 1
		tiempo -= 0.03

		if score > high_score:
			high_score = score


		marcador.clear()
		marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Arial", 20))

	# Mover el cuerpo de la serpiente
	distance_body = len(body)

	for i in range(distance_body -1, 0, -1):
		x = body[i-1].xcor()
		y = body[i-1].ycor()
		body[i].goto(x,y)

	if distance_body > 0:
		x = head.xcor()
		y = head.ycor()
		body[0].goto(x,y)

# Haciendo que las flechas dirijan 

	mov()

	# Colisiones con el cuerpo

	for i in body:
		if i.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = 'stop'

			for i in body:
				i.goto(900,900)

			body.clear()

			score = 0
			marcador.clear()
			marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Arial", 20))


	time.sleep(tiempo)							# Con la librería 'time' podemos retrasar la ejecución del while

ventana.exitonclick()