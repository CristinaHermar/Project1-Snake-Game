import turtle
import time
import random
import os


# resources :
#bgpic = 'C:/Users/Iron/Pictures/fondo-snake2.jpg'


#win = turtle.Screen()
#win.addshape(bgpic)

#sh = turtle.Turtle()
#sh.shape(bgpic)

# Shuting the window down :
#turtle.mainloop()

# Area de juego

ventana = turtle.Screen()
ventana.title(' Juguemos Snake ')
ventana.bgcolor('white')
ventana.setup(width = 700, height = 700)
ventana.tracer(0)								# Hace animaciones mas interactivas con el usuario
#ventana.addshape(bgpic)
# Head

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.penup()									# Con este método no deja rastro nuestro elemento
head.goto(0,0)
head.direction = 'stop'

# Food

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
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
marcador.write('Score:  0    Hight Score: 0 ', align="center", font = ("Lemon", 20, "normal"))

# Funciones

def arriba():
	head.direction = 'up'

def abajo():
	head.direction = 'down'

def derecha():
	head.direction = 'right'

def izquierda():
	head.direction = 'left'

def exit():
	ventana.bye()

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

def quitartiempo(x,y):
	if x == 0.05:
		y = y + 0.05
		return y

# Haciendo que las flechas dirijan 
ventana.listen()							# Esta funcion '.listen' permite que la ventana de trabajo capte las entradas del teclado, como un input'
ventana.onkeypress(arriba, 'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(derecha, 'Right')
ventana.onkeypress(izquierda, 'Left')
ventana.onkeypress(exit,'x')
## Definir niveles

tiempo = 0.15
nuevo_tiempo = tiempo

while True:
	ventana.update()

	# Colisiones bordes

	if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
		time.sleep(1)
		tiempo = 0.15
		nuevo_tiempo = tiempo	
		head.goto(0,0)
		head.direction = 'stop'

		for i in body:
			i.goto(900,900)

		body.clear()

		#Resetear marcador

		score = 0
		marcador.clear()
		marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Lemon", 20, "normal"))


		
	if head.distance(food) < 20:
		x = random.randint(-330, 330)
		y = random.randint(-330, 300)
		food.goto(x,y)


		new_body = turtle.Turtle()
		new_body.speed(0)
		new_body.shape('square')
		new_body.color('black')									
		new_body.penup()
		body.append(new_body)


		score += 1
		tiempo -= 0.01
		nuevo_tiempo = tiempo
		
		if score > high_score:
			high_score = score
		
		if len(body) > 12:
			nuevo_tiempo = 0.025


		marcador.clear()
		marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Lemon", 20, "normal"))

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

			tiempo = 0.15
			nuevo_tiempo = tiempo	

			for i in body:
				i.goto(900,900)

			body.clear()

			score = 0
			marcador.clear()
			marcador.write("Score:  {}    Hight Score: {} ".format(score, high_score) , align="center", font = ("Arial", 20))

		
	time.sleep(nuevo_tiempo)							# Con la librería 'time' podemos retrasar la ejecución del while
	
