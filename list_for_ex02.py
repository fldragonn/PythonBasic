# list_for_ex02.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 5명의 성적 리스트 grades 만들기
grades = [80, 95, 77, 82, 99]

# 5명의 리스트 총점, 평균 구하기
# 총점: sum_g, 개수: cnt_g, 평균: avg_g

# 총점, 개수 변수 초기화
sum_g = 0
cnt_g = 0

for value in grades:
    sum_g = sum_g + value
    cnt_g = cnt_g + 1
    print("{}번: {}점".format(cnt_g, value))

avg_g = sum_g / cnt_g

print()
print("학급 총점은 {}점이고, 평균은 {}점이다.".format(sum_g, avg_g))
