# list_for_04.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 복권 번호 생성기
# 1~45까지 무작위로 6개의 수를 추출하기

import random as r

# 복권 번호 리스트 생성
l_list = list()

# 번호 선정 개수 변수 cnt 초기화
cnt = 0
while cnt < 6:
    num = r.randint(1, 45)
    if num not in l_list:
        print("새로운 번호를 추가합니다: ", num)
        l_list.append(num)
        cnt = cnt + 1
        print(num, l_list)
    else:
        print("번호 중복: ", num)