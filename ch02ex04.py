# 도형 함수 만들기
# moveT(x, y)
# drawPoly(n, d, x, y)

import turtle as t

def moveT(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def drawPoly(n=4, d=50, x=0, y=0):
    moveT(x, y)
    for x in range(n):
        t.forward(d)
        t.right(360/n)

drawPoly()
drawPoly(8, 30, 100, 100)
drawPoly(5, 50)

t.mainloop()