# 기본입출력
# 화폐 교환기

num = int(input("교환할 금액을 입력하세요: "))

print()
tmp = num
print("교환금액: ", num)
print("50000원: ", tmp // 50000)
tmp = tmp % 50000
print("10000원: ", tmp // 10000)
tmp = tmp % 10000
print("5000원: ", tmp // 5000)
tmp = tmp % 5000
print("1000원: ", tmp // 1000)
tmp = tmp % 1000
print("기타: ", tmp)


