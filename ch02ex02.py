# step2. n px 도형 그리기
# drawRect(n), drawTri(n)
# 길이 초기 값 설정하기 (n = 50)

import turtle as t

def drawRect(n=50):
    for x in range(4):
        t.forward(n)
        t.right(90)

def drawTri(n):
    for x in range(3):
        t.forward(n)
        t.right(120)

drawRect(100)
drawRect()
drawTri(50)