# step2. n px 도형 그리기
# drawRect(n), drawTri(n)

import turtle as t

def drawRect(n):
    for x in range(4):
        t.forward(n)
        t.right(90)

def drawTri(n):
    for x in range(3):
        t.forward(n)
        t.right(120)

drawRect(100)

t.up()
t.goto(100, 0)
t.down()
drawTri(50)