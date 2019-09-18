# 도형 함수 만들기
# step3. 특정 위치에 도형 그리기
# drawRect, drawTri

import turtle as t

def drawRect(x=0, y=0, n=50):
    t.up()
    t.goto(x, y)
    t.down()

    for x in range(4):
        t.forward(n)
        t.right(90)

def drawTri(x=0, y=0, n=50):
    t.up()
    t.goto(x, y)
    t.down()
    for x in range(3):
        t.forward(n)
        t.right(120)

drawRect(100, 100, 100)
drawTri(-100, -100, 200)