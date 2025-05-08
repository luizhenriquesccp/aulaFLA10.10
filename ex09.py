import turtle
rick = turtle.Turtle()

def desenhe_hexagono():
    for _ in range(4):
        rick.forward(25)
        rick.right(90)
       
for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            desenhe_hexagono()
            rick.penup()
            rick.forward(75)
            rick.pendown()
        rick.penup()
        rick.backward(25)
        rick.pendown()
        rick.right(60)
        rick.penup()
        rick.forward(25)
        rick.pendown()
        rick.right(120)
    rick.penup()
    rick.backward(25)
    rick.pendown()
    rick.left(60)
    rick.penup()
    rick.forward(50)
    rick.pendown()
    rick.right(60)
