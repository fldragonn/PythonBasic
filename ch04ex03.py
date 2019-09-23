# 난수를 사용해 덧셈, 뺄셈 문제 만들기
# 함수명: makeQuiz()
# 함수 반환값
# 14 - 3
# 12 + 7
# 조건1: 문제 첫 수는 10~20사이의 난수
# 조건2: 문제 두 번째 수는 1~9사이의 난수
# 조건3: 연산자 결정은 1~2사이 난수 (1: +, 2: -)

import random as r

def makeQuiz():
    num1 = r.randint(10, 20)
    num2 = r.randint(1, 9)
    op = r.randint(1, 2)

    quiz = str(num1)
    if op == 1:
        quiz = quiz + "+"
    else:
        quiz = quiz + "-"
    quiz = quiz + str(num2)

    return quiz

for x in range(5):
    quiz = makeQuiz()
    print(quiz, "=", eval(quiz))