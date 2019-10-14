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
for value in grades:
    value = value + 5
    print(value)

# 원본 리스트 출력하기
print("Grages: ", grades)