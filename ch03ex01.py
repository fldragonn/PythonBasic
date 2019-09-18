# 태극 모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

color = ['red', 'yellow', 'blue', 'green']
for x in range(300):
    t.color(color[x % 4])
    t.forward(x * 2)
    t.left(89)

t.mainloop()