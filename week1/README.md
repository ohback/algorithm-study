# 1주차 자료 — 준비 & 기초 문법

> **주제**: 표준 입출력 · 조건문 · 반복문 · 기초 연산 · 기초 수학<br>
> **목표:** 20–25문제 풀이로 입출력/반복 패턴에 완전 적응
> 

---

## 0) 시작 가이드

### 필수 세팅

- **빠른 입력**: 큰 입력에서는 `sys.stdin.readline`을 습관화
- **기본 템플릿**

```python
import sys

def main():
    input = sys.stdin.readline  # 빠른 입력
    # 코드 작성

if __name__ == "__main__":
    main()

```

### 파이썬 기본 문법 리마인드

- 공백/개행 구분: `input().split()` → 공백 기준 / `strip()`으로 개행 제거
- 정수 변환: `a, b = map(int, input().split())`
- 반복 출력 최적화: 리스트에 모아 `"\n".join(map(str, arr))`

---

## 1) 표준 입출력 (I/O) 패턴

| 패턴 | 설명 | 예시 코드 |
| --- | --- | --- |
| 한 줄에 두 정수 | 공백으로 분리 | `a, b = map(int, input().split())` |
| 여러 줄, 고정 개수 | 반복문으로 N줄 처리 | `for _ in range(N): ...` |
| EOF까지 입력(끝 모를 입력) | 파일 끝날 때까지 | `for line in sys.stdin: ...` |
| 센티넬 종료 | 특정 값 나오면 중단 | `while True: ... if a==0 and b==0: break` |
| 빠른 출력 | 많을 때 합쳐서 출력 | `print("\n".join(buf))` |

**EOF 패턴(10951형):**

```python
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

```

**센티넬 패턴(10952형):**

```python
import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)

```

**빠른 입력 요구(15552형):**

```python
import sys
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    a, b = map(int, input().split())
    out.append(str(a + b))
print("\n".join(out))

```

---

## 2) 조건문 & 반복문 핵심

### 조건문

- 중첩 최소화, 조기 종료(guard clauses) 활용

```python
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

```

### 반복문

- 범위 주의: `range(n)`은 0..n-1
- 역순: `for i in range(n, 0, -1):`
- 누적합: `total = sum(range(1, n+1))` (학습 목적상 직접 for문도 연습)

---

## 3) 기초 연산 & 기초 수학

### 나머지 연산(10430형)

- `(A+B)%C == ((A%C) + (B%C)) % C`
- `(A×B)%C == ((A%C) × (B%C)) % C`

### 최대공약수(GCD) & 최소공배수(LCM) (2609형)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    g = gcd(a, b)
    return a // g * b

```

### 소수(Prime) & 에라토스테네스의 체 (1978, 1929형)

- **체 알고리즘(구간 소수 출력에 필수)**

```python
def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p*p <= n:
        if is_prime[p]:
            for q in range(p*p, n+1, p):
                is_prime[q] = False
        p += 1
    return is_prime

```

---

## 4) 문제별 가이드 (링크 & 핵심 포인트)

> 각 링크는 Baekjoon 문제 페이지로 이동합니다.
> 

### A. 워밍업 & 입출력/반복

- 2557 Hello World — 기본 출력
- 1000 A+B — 한 줄 두 수
- 2558 A+B - 2 — 두 줄 입력
- 2739 구구단 — 단순 반복
- 10950 A+B - 3 — 테스트케이스 반복
- 8393 합 — 1..n 합 (for문 or `n*(n+1)//2`)
- 15552 빠른 A+B — `sys.stdin.readline` 필수
- 2741 N 찍기 — 1..N 출력
- 2742 기찍 N — N..1 출력

**출력 포맷 유의(케이스 넘버링)**

- 11021 A+B - 7, 11022 A+B - 8

```python
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")                # 11021
    # print(f"Case #{i}: {a} + {b} = {a+b}")  # 11022

```

**별 찍기(정렬/공백)**

- 2438 별 찍기 - 1 — 왼쪽 정렬
- 2439 별 찍기 - 2 — 오른쪽 정렬(공백)

```python
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)   # 2439

```

**조건 필터/리스트 출력**

- 10871 X보다 작은 수

```python
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(*[v for v in arr if v < x])  # 공백 구분 출력

```

**입력 종료 패턴**

- 10952 A+B - 5 — 센티넬(0 0)
- 10951 A+B - 4 — EOF

### B. 연산/수학

- 10430 나머지 — 모듈러 성질 확인
- 2609 최대공약수와 최소공배수 — 유클리드 호제법
- 1978 소수 찾기 — 소수 판별
    - 소수 판별은 **√n까지만** 나눠보면 충분
- 1929 소수 구하기 — 구간 소수, **체 사용**

```python
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
prime = [True]*(n+1)
prime[0]=prime[1]=False
p=2
while p*p<=n:
    if prime[p]:
        for q in range(p*p, n+1, p):
            prime[q]=False
    p+=1

out=[]
for x in range(m, n+1):
    if prime[x]:
        out.append(str(x))
print("\n".join(out))

```

---

## 5) 체크리스트

- [ ]  `sys.stdin.readline`과 기본 `input()`의 차이를 이해했다.
- [ ]  EOF/센티넬 종료 입력을 코드로 구현할 수 있다.
- [ ]  `for`, `while`을 상황에 맞게 선택하여 사용했다.
- [ ]  문자열 포맷팅(f-string)과 출력 형식을 정확히 맞췄다.
- [ ]  GCD/LCM, 소수 판별, 체 알고리즘을 구현했다.
- [ ]  별 찍기에서 공백 처리로 정렬을 정확히 맞췄다.

---

## 6) 이번 주 과제 (필수)

아래 **20문제**를 모두 풀이하세요.

2557, 1000, 2558, 2739, 10950, 8393, 15552, 2741, 2742, 11021, 11022, 2438, 2439, 10871, 10952, 10951, 10430, 2609, 1978, 1929

> 권장: 풀이 후 스스로 입출력 패턴 분류, 시간복잡도 한 줄 정리, 실수 기록을 남기세요.
>