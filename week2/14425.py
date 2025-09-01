# n, m 입력 받기
# 집합 s = set()
# n개만큼 입력 받아서 집합 s 넣기
# 문자열 개수 세는 용도로 count = 0 세팅
# m개 입력 받아서 변수에서 저장
# m이 s에 포함되었다면 카운트 증가
# 최종 개수 출력


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = set()

for _ in range(n):
    s.add(input().rstrip())

count = 0
for _ in range(m):
    check_str = input().rstrip()
    if check_str in s:
        count += 1

print(count)