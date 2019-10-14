# list_fun.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 성적 리스트 grades 만들기
grades = [95, 75, 85, 65]

# 함수를 사용해 총점, 평균 구하기
sum_g = sum(grades)
avg_g = sum(grades) / len(grades)
print("학급 총점은 {}점 이고, 평균은 {}점이다.".format(sum_g, avg_g))
