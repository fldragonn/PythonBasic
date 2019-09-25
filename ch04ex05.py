
# 덧셈, 뺄셈 문제 만들기

import random as r

def makeQuiz():
    num1 = r.randint(10, 20)
    num2 = r.randint(1, 9)
    op = r.randint(1, 2)
    if op == 1:
        op_str = "+"
    else:
        op_str = "-"
    quiz = "{}{}{}".format(num1, op_str, num2)
    return quiz

for x in range(5):
    quiz = makeQuiz()
    print(quiz, "=", eval(quiz))
