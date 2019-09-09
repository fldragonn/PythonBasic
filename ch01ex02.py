# 간단 계산기
# 두 수를 입력 받아 덧셈, 나눗셈, 몫을 구하는 프로그램 만들기

num1 = int(input("정수를 입력하세요: "))
num2 = int(input("정수를 입력하세요: "))

print()
print("{}과 {}을 더하면 {}입니다.".format(num1, num2, num1 + num2))
print("{}과 {}을 나누면 {}입니다.".format(num1, num2, num1 / num2))
print("{}과 {}을 나눈 몫은 {}입니다.".format(num1, num2, num1 // num2))

# 형식지정자
print()
print("%d와 %d를 더하면 %d입니다." % (num1, num2, num1 + num2))
print("%d와 %d를 나누면 %.1f입니다." % (num1, num2, num1 / num2))
print("%d와 %d를 나눈 몫은 %d입니다." % (num1, num2, num1 // num2))