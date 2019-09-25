# 뺄셈 문제 만들기
# ch04ex01.py

import random as r

def makeQuiz():
    num1 = r.randint(10, 20)
    num2 = r.randint(1, 10)
    quiz = "{}-{}".format(num1, num2)
    return quiz

for x in range(5):
    quiz = makeQuiz()
    usr_ans = int(input(quiz+"="))
    if usr_ans == eval(quiz):
        print("correct!")
    else:
        print("incorrect!")