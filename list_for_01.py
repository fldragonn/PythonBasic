# list_for_01.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 5명의 성적 리스트 grades 만들기
grades = [80, 90, 70, 100, 50]

# 리스트 내의 각 원소출력하기
print("리스트 값 하나씩 출력하기")
for value in grades:
    print(value)

# 리스트 내의 원소에 인덱스로 접근하기
# len(리스트): 리스트 원소 개수 구하기
print()
print("리스트 값 인덱스를 이용해 출력하기")
list_cnt = len(grades)
for idx in range(list_cnt):
    print("index: ", idx, "value: ", grades[idx])

# 인덱스와 값을 한번에 접근하기
print()
print("리스트의 값, 인덱스를 한 번에 출력하기")
for idx, value in enumerate(grades):
    print("index: ", idx, "value: ", value)


