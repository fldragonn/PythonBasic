# ch04ex06.py
# 리스트로 문제 만들기

import random as r

def makeQuiz():
    num1 = r.randint(10, 20)
    num2 = r.randint(1, 9)
    op = r.randint(0, 2)

    quiz = "{}{}{}".format(num1, ['+', '-', '*'][op], num2)
    return quiz

for x in range(5):
    quiz = makeQuiz()
    print(quiz, "=", eval(quiz))
