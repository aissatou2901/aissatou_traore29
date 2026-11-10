import turtle

t = turtle.Turtle()
t.speed(0)

couleurs = ["red", "orange", "yellow", "magenta", "brown"]

def dessiner_petale():
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)

# La tige (dessinée en premier, pour être derrière les pétales)
t.color("green")
t.pensize(8)
t.setheading(-90)
t.forward(250)

# Retour au centre sans dessiner
t.penup()
t.home()
t.pendown()
t.pensize(1)

# Les pétales
for i in range(60):
    t.color(couleurs[i % len(couleurs)])
    t.begin_fill()
    dessiner_petale()
    t.end_fill()
    t.left(6)

turtle.done()