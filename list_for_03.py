# list_for_03.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 성적 리스트 grades 만들기
grades = [95, 75, 85, 65]

# 원본 리스트 출력
print("Grages: ", grades)

# 각 성적을 수정해 출력하기
print("각 성적을 5점씩 추가해 출력하기")
for value in grades:
    value = value + 5
    print(value)

# 원본 리스트 출력하기
print("Grages: ", grades)

# 원본 리스트 자료 값 수정하기
print()
print("실제 리스트 원소 값 수정하기")

# 리스트 원소 개수 구하기
cnt = len(grades)

# 각 학생 성적 5점씩 추가하기
for idx in range(cnt):
    grades[idx] = grades[idx] + 5

# 수정 리스트 출력하기
print("Grages: ", grades)
