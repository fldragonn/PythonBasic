# 기본 입출력
# 채팅 봇 만들기

# 1
# print
print("안녕하세요? 저는 pitca bot입니다.")
print()
name = input("당신의 이름을 알려주세요: ")
age = int(input(str(name) + ", 당신의 나이는? "))
print()
print("환영합니다. ", name, "님!")
print("당신은 다음해에 ", age + 1, "살이 되는군요!")
print()

# 2
# 형식 문자(%s, %d 사용하기)
print("안녕하세요? 저는 pitca bot입니다.")
print()
name = input("당신의 이름을 알려주세요: ")
age = int(input("%s, 당신의 나이는? " % name))
print()
print("환영합니다. %s님!" % name)
print("당신은 다음해에 %d살이 되는군요!" % (age + 1))
print()

# 3
# format
print("안녕하세요? 저는 pitca bot입니다.")
print()
name = input("당신의 이름을 알려주세요: ")
age = int(input("{}, 당신의 나이는? ".format(name)))
print()
print("환영합니다. {}님!".format(name))
print("당신은 다음해에 {}살이 되는군요!".format(age + 1))
print()
