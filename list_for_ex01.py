# list_for_01.py
#
# 평촌아이티
# www.pitca.co.kr
#
# 5명의 성적 리스트 grades 만들기
grades = [80, 95, 77, 82, 99]

# 번호와 성적 출력하기
for num, one in enumerate(grades):
    print("{}번 {}".format(num + 1, one))