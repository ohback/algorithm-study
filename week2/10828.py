# n 입력 받고
# stack=[] 리스트 만들어주고
# n만큼 for문 돌리고
# 명령 n개 입력 받고
# if문으로 push, pop, size, empty ,top 작업 수행

import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())    
    
    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])





