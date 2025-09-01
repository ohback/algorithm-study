# n, k 입력 받기
# 1부터 n까지 저장할 queue 만들어주기
# 수열 출력을 위한 지워진 숫자 저장 리스트 만들기 result = []
# while > 0 까지 반복하기
# for _ in range(k-1)
# front_person = queue.popleft()
# queue.append(front_person)
# removed_person = queue.popleft()
# result.append(removed_person)
# print

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n+1))
result = []

while len(queue) > 0:
    for _ in range(k-1):
        front_person = queue.popleft()
        queue.append(front_person)

    removed_person = queue.popleft()
    result.append(removed_person)

print("<" + ', '.join(map(str, result)) + ">")