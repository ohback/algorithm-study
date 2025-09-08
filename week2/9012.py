import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    ps = input().rstrip()
    is_vps = True
    
    for char in ps:
        if char == '(':
            stack.append(char)
            
        elif char == ')':
            if not stack:
                is_vps = False
                break               
            else:
                stack.pop()
    
    if stack:
        is_vps = False
            
    if is_vps:
        print("YES")
    else:
        print("NO")