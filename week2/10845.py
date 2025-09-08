import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque()
result = []

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if not queue:
            result.append(-1)
        else:
            queue.popleft()
    elif command[0] == 'size':
        print(len(result))
    elif command[0] == 'empty':
        if not command:
            print("1")
        else:
            print("0")
    elif command[0] == 'front':
        front_int = result.popleft()
        if not command:
            print("-1")
        else:
            print(front_int)
    elif command[0] == "back":
        rear_int = result.popright()
        if not command:
            print("-1")
        else:
            print(rear_int)
