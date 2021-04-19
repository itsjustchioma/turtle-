import turtle 
color = ['#9c6644', '#7f5539', '#b08968', '#ddb892', '#e6ccb2', '#ede0d4']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(360000):
    t.pencolor(color[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)