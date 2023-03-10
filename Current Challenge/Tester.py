import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.setup(800, 800)
turtle.bgcolor('black')
for x in range(10000):
    turtle.pencolor(colors[x % 6])
    turtle.width((x / 100) + 1)
    turtle.forward(x)
    turtle.left(10)
turtle.done()