# 난수를 이용해 덧셈 문제 만들기
# str() 함수, + 연산자 사용
# 출력 예시: 3 + 5 = 8

import random as r

num1 = r.randint(10, 20)
num2 = r.randint(1, 10)

quiz = str(num1) + "+" + str(num2)
ans = num1 + num2

print(quiz, "=", ans)
