# 카드 갯수 n 입력 받고
# 큐 만들어주기
# 마지막 1장 남을 때까지 반복(While)
# 가장 앞에 있는 카드 버리기 popleft()
# card = queue.popleft()로 맨 앞 카드 저장
# append()로 맨뒤에 추가
# print(queue[0])



import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    queue.popleft()

    card = queue.popleft()
    queue.append(card)

print(queue[0])
