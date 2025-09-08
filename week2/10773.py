import sys

input = sys.stdin.readline

k = int(input())

money = []

for _ in range(k):
    num = int(input())
              
    if num == 0:
       money.pop()
    else:
       money.append(num)
              
print(sum(money))