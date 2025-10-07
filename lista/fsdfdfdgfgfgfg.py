import turtle
import random

# Configura o screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Coração e Estrelas")

# Cria um turtle para desenhar
pen = turtle.Turtle()
pen.speed(0) # Velocidade máxima
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.pendown()

# Define a string para o nome
nome_usuario = input("Digite seu nome: ")

# Desenha o coração
pen.fillcolor("red")
pen.begin_fill()
pen.left(140)
pen.forward(180)
for _ in range(2):
    pen.circle(-90, 200)
    pen.left(120)
pen.end_fill()
pen.penup()

# Posiciona o texto
pen.goto(0, -150)
pen.pencolor("white")
pen.write(nome_usuario, align="center", font=("Arial", 24, "bold"))
pen.hideturtle()

# Função para desenhar uma estrela individual
def desenha_estrela(x, y, tamanho):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("yellow")
    for _ in range(5):
        pen.forward(tamanho)
        pen.right(144) # Ângulo para um pentagrama
    pen.penup()

# Desenha várias estrelas no fundo
num_estrelas = 50
for _ in range(num_estrelas):
    x_aleatorio = random.randint(-280, 280)
    y_aleatorio = random.randint(-280, 200) # Ajusta para não cobrir o coração
    tamanho_aleatorio = random.randint(5, 15)
    desenha_estrela(x_aleatorio, y_aleatorio, tamanho_aleatorio)

screen.mainloop() # Mantém a janela aberta