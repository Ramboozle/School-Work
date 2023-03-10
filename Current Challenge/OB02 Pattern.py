import turtle
dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/patterns.txt'

class Pattern:
    def __init__(self,angle,times):
        self.__angle = angle
        self.__times = times

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 800)
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width((x / 100) + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

    def __repr__(self):
        return self.__angle
        return self.__times

with open(dir, 'r') as f:
    LinesNum = int(len(f.readlines())/2)
def ReadLine(line):
    with open(dir,'r') as f:
        return f.readline(line)

Patterns = []
for i in range(4):
    print(2*i,2*i+1)
    Patterns.append(Pattern(ReadLine(2*i),ReadLine(2*i+1)))
    Patterns[i].draw_pattern()