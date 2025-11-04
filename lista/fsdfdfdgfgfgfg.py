import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Coração e Estrelas")

pen = turtle.Turtle()
pen.speed(0) 
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.pendown()

nome_usuario = input("Digite seu nome: ")


pen.fillcolor("red")
pen.begin_fill()
pen.left(140)
pen.forward(180)
for _ in range(2):
    pen.circle(-90, 200)
    pen.left(120)
pen.end_fill()
pen.penup()

pen.goto(0, -150)
pen.pencolor("white")
pen.write(nome_usuario, align="center", font=("Arial", 24, "bold"))
pen.hideturtle()


def desenha_estrela(x, y, tamanho):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("yellow")
    for _ in range(5):
        pen.forward(tamanho)
        pen.right(144) 
    pen.penup()

num_estrelas = 50
for _ in range(num_estrelas):
    x_aleatorio = random.randint(-280, 280)
    y_aleatorio = random.randint(-280, 200) 
    tamanho_aleatorio = random.randint(5, 15)
    desenha_estrela(x_aleatorio, y_aleatorio, tamanho_aleatorio)

screen.mainloop()