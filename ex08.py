import turtle

leo = turtle.Turtle()

def flores ():
    for _ in range(6):
    	
    	for _ in range(8):
    		leo.forward(20)
    		leo.right(30)
    	leo.right(60)
    
for _ in range(3):
	flores()
	leo.penup()
	leo.forward(150)
	leo.pendown()
	