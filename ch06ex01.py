# ch06ex01.py
# 리스트에서 무작위 원소 추출하기

import random

# 단어 리스트(타자 연습에 사용할 단어 목록)와 문제 번호 설정
word_list = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
quiz_number = 1

# 랜덤하게 5단어 출력하기
for x in range(5):
    word_num = random.randint(1, 5)
    print(x+1, word_list[word_num])

print()

# 랜덤하게 5단어 출력하기
for x in range(5):
    word = random.choice(word_list)
    print(x+1, word)