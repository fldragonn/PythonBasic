# list_for_ex03.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 5명의 성적 리스트 grades 만들기
grades = [80, 95, 77, 82, 99]

# 학생 성적표 총점, 평균 구하기
# 원본 성적 우선 출력
for idx, one in enumerate(grades):
    print("{}번 {}점".format(idx, one))

print()
print("성적 업데이트 후")

# 리스트 개수 추출
cnt = len(grades)

for idx in range(cnt):
    grades[idx] += 5
    if grades[idx] >= 100: grades[idx] = 100
    print("{}번 {}점".format(idx, grades[idx]))