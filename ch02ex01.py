# 도형 함수 만들기
# step1. 한 변이 50px인 도형 그리기
# drawRect, drawTri

import turtle as t

def drawRect():
    for x in range(4):
        t.forward(50)
        t.right(90)

def drawTri():
    for x in range(3):
        t.forward(50)
        t.right(120)

drawRect()
drawTri()