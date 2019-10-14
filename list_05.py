# list_05.py
#
# 평촌아이티
# www.pitca.co.kr
#

# 복권 번호 생성기
# 1~45까지 무작위로 6개의 수를 추출하기

import random as r

# 1~45까지 원소를 갖는 복권 번호 리스트 생성
l_list = list(range(1, 46))
print("복권 번호 모음: ", l_list)

# 복권 리스트 섞기
r.shuffle(l_list)
print("복권 번호 섞기: ", l_list)

# 복권 번호 추출하기
print("번호 추첨: ", l_list[:6])