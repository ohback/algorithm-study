# 3주차 자료 — 정렬 & 탐색

> 주제
>- 기초 정렬: 버블, 선택, 삽입  
>- 고급 정렬: 퀵, 병합, 힙, (파이썬 내장 TimSort)  
>- 탐색: 선형 탐색, 이진 탐색(기본/응용: 파라메트릭 서치)  
>
> 목표
> - **정렬 알고리즘의 개념/차이/시간복잡도**를 이해하고, 파이썬 내장 정렬을 >안전하게 활용한다.
>- **선형 탐색 vs 이진 탐색**의 차이와 사용 조건(정렬 여부)을 구분한다.
>- 백준 실습을 통해 **입출력 최적화, 키 정렬, 안정 정렬, 파라메트릭 서치>(이분 탐색 응용)**를 체득한다.

---

## 1. 정렬 알고리즘 한눈에 보기

| 알고리즘 | 아이디어 | 평균/최악 | 특징/비고 |
|---|---|---:|---|
| 버블 정렬 | 인접 원소를 비교/교환 | O(n²) | 구현 쉬움.|
| 선택 정렬 | 매 단계 최소값 선택 후 앞에 배치 | O(n²) | 교환 횟수 적음. |
| 삽입 정렬 | 이미 정렬된 구간에 삽입 | 평균 O(n²), 최선 O(n) | **거의 정렬된 데이터**에 강함 |
| 퀵 정렬 | 분할 정복, 피벗 기준 분할 | 평균 O(n log n), 최악 O(n²) | 제자리(in-place) 구현 가능. 피벗 전략 중요 |
| 병합 정렬 | 반 나누고 병합 | O(n log n) | 안정 정렬, 추가 메모리 O(n) |
| 힙 정렬 | 힙 자료구조 이용 | O(n log n) | 최악에도 보장, 제자리 가능(불안정) |
| **파이썬 sort** | **TimSort** | O(n log n) | **안정 정렬**, 거의 정렬된 데이터 최적화, 키 정렬 지원 |

### 1-1. 정렬 알고리즘 상세 & 예제
#### A) 버블 정렬 (Bubble Sort)
- **아이디어**: 이웃한 두 원소를 비교해 큰 값을 오른쪽으로 "거품처럼" 밀어 올림.
- **복잡도**: 평균/최악 O(n²), 최선(이미 정렬) O(n) — *스왑 없음 조기 종료 시*
- **성질**: 제자리(in-place), **안정적(stable)**
- **언제?** 거의 정렬된 소규모 데이터 학습용
```python
def bubble(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:  # 더 이상 교환이 없으면 조기 종료
            break
```

#### B) 선택 정렬 (Selection Sort)
- **아이디어**: 남은 구간에서 **최솟값**을 골라 현재 위치와 교환
- **복잡도**: 항상 O(n²)
- **성질**: 제자리, **불안정(unstable)** (동일 키의 상대 순서가 바뀔 수 있음)
- **언제?** 스왑 횟수가 적어야 하는 특수 상황(이론/학습)
```python
def selection(a):
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
```

#### C) 삽입 정렬 (Insertion Sort)
- **아이디어**: 앞쪽의 **정렬된 부분**에 현재 원소를 **올바른 위치**에 삽입
- **복잡도**: 평균/최악 O(n²), 최선 O(n)
- **성질**: 제자리, **안정적(stable)**
- **언제?** **거의 정렬된 데이터**, 작은 입력에서 매우 효율적
```python
def insertion(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
```

#### D) 퀵 정렬 (Quick Sort)
- **아이디어**: 피벗을 기준으로 **작은 것 / 큰 것**으로 분할하여 재귀 정렬 (분할정복)
- **복잡도**: 평균 O(n log n), **최악 O(n²)** (피벗 선택이 나쁘면)
- **성질**: 보통 제자리(in-place) 구현 가능, **불안정**
- **언제?** 일반적으로 매우 빠름(좋은 피벗 선택/랜덤화)
```python
# 중앙값 피벗의 Hoare 방식 분할 (간단하고 빠른 편)
def quicksort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return
    pivot = a[(lo + hi) // 2]
    i, j = lo, hi
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1; j -= 1
    if lo < j:
        quicksort(a, lo, j)
    if i < hi:
        quicksort(a, i, hi)
```
> 팁: **무작위 피벗**이나 **중앙값 피벗**을 쓰면 최악 케이스 위험을 완화할 수 있습니다.

#### E) 병합 정렬 (Merge Sort)
- **아이디어**: 배열을 반으로 나눠 각각 정렬 후 **병합**
- **복잡도**: 항상 O(n log n)
- **성질**: **안정적**, 추가 메모리 O(n)
- **언제?** 안정성 필요, 링크드 리스트/외부정렬, 파이썬 TimSort의 기반 아이디어와 친척격
```python
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    # 병합 단계
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 안정성 유지
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

# 사용 예
# a = [5,3,1,4,2]
# a = merge_sort(a)
```

#### F) 힙 정렬 (Heap Sort)
- **아이디어**: 힙(완전이진트리)으로 **최솟값/최댓값**을 빠르게 꺼내 정렬
- **복잡도**: O(n log n)
- **성질**: 제자리 구현 가능(불안정). 파이썬 `heapq`는 **최소 힙** 제공
- **언제?** 최악에도 O(n log n) 보장 필요할 때
```python
# 간단 버전: heapq로 오름차순 정렬 리스트 만들기
import heapq

def heap_sort(iterable):
    h = []
    for x in iterable:
        heapq.heappush(h, x)
    out = []
    while h:
        out.append(heapq.heappop(h))
    return out

# 사용 예
# print(heap_sort([5,3,1,4,2]))  # [1,2,3,4,5]
```

> 참고: **내장 정렬(TimSort)**는 실제 데이터의 **부분 정렬(run)**을 감지해 더 빠르게 동작하며, **안정 정렬**입니다. 실전 코테에서는 내장 정렬을 최우선으로 고려하세요.

---

## 2. 파이썬 정렬 사용법
```python
# 기본 오름차순
arr.sort()
# 또는: arr_sorted = sorted(arr)

# 내림차순
arr.sort(reverse=True)

# 키 정렬 (예: 문자열 길이→사전순)
words = ["but", "i", "wont", "hesitate"]
words.sort(key=lambda w: (len(w), w))

# 다중 키: 좌표 (x, y)
pts = [(3,4), (1,7), (1,2)]
pts.sort(key=lambda p: (p[0], p[1]))
```

### 안정 정렬(Stable Sort)
- 파이썬 정렬은 **안정적**입니다: **같은 키**의 원소는 **입력 순서 유지**.  
→ `10814 (나이순 정렬)`에서 매우 중요.

### 입출력/메모리 팁
```python
import sys
input = sys.stdin.readline
print = sys.stdout.write  # 대량 출력 시
```

---

## 3. 선형 탐색 (Linear Search)
- **아이디어**: 왼쪽부터 오른쪽으로 **하나씩 스캔**하며 조건을 만족하는 원소를 찾는다.
- **전제**: 정렬 **불필요**. 한 번 훑으면 됨.
- **복잡도**: 시간 O(n), 추가 메모리 O(1)

```python
# 1) 값의 존재 여부 / 위치 반환 (-1이면 없음)
def linear_search(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1

# 존재 여부만 필요할 때 (True/False)
exists = any(v == 42 for v in [10, 42, 7])

# 2) 마지막 위치 찾기
def find_last(a, x):
    for i in range(len(a)-1, -1, -1):
        if a[i] == x:
            return i
    return -1

# 3) 조건 기반 찾기 (predicate)
from typing import Callable

def find_if(a, pred: Callable[[int], bool]):
    for i, v in enumerate(a):
        if pred(v):
            return i
    return -1

# 예: 처음으로 짝수인 원소의 인덱스
idx = find_if([3, 5, 8, 1], lambda x: x % 2 == 0)

# 4) 개수/최솟값/최댓값 (단일 스캔)
arr = [5, 1, 7, 1, 9]
count_small = sum(1 for v in arr if v < 3)   # 조건을 만족하는 원소 개수
min_val, min_idx = min((v, i) for i, v in enumerate(arr))
max_val, max_idx = max((v, i) for i, v in enumerate(arr))

# 5) 스트리밍 입력에서의 조기 종료 (백준 입출력 예)
import sys
for line in sys.stdin:
    x = int(line)
    if x == 0:
        break  # 특정 조건을 만나면 탐색 종료
```

**언제 쓰나?**
- 데이터가 **작거나**, 탐색이 **한두 번**만 필요한 경우
- **정렬이 불가능**하거나 원본 순서를 유지해야 하는 경우
- 빠른 **프로토타이핑**/직관적인 코드가 필요한 경우

**언제 피하나?**
- 데이터가 **크고** 탐색 **질의가 많을 때** → `set`으로 해시 조회(O(1)) 또는 한 번 정렬 후 **이진 탐색(O(log n))**

---

## 4. 이진 탐색 (Binary Search)
- **전제: 정렬된 배열**. 중앙을 기준으로 범위를 절반씩 줄여 감.
- 시간복잡도: O(log n)

```python
# 기본(존재 여부)
def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```

### 파라메트릭 서치(매개변수 탐색)
- **"조건을 만족하는 값의 최댓값/최솟값"**을 이분으로 찾는 패턴.  
예) `2805 (나무 자르기)`: "절단 높이"를 이분 탐색.  
예) `2110 (공유기 설치)`: "최소 거리"를 이분 탐색.

```python
# 최대 높이 h: sum(max(0, tree-h)) >= M 를 만족
def max_height(trees, M):
    lo, hi = 0, max(trees)
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        got = sum((t - mid) for t in trees if t > mid)
        if got >= M:      # 더 많이 잘렸으면 높이를 올려 본다
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
```

---

## 5. 실습: 백준 문제 가이드
> 문제 번호만 제공합니다. 제목/입력 형식은 백준에서 확인하세요.

### 정렬 기초/대량 정렬
- **2750 (수 정렬하기)**: 정렬 기본. `sorted()` 출력.
- **2751 (수 정렬하기 2)**: 데이터 많음. `sys.stdin.readline` + `sorted` 사용. `print("\n".join(...))`로 한 번에 출력.
- **10989 (수 정렬하기 3)**: 값 범위가 **1~10000** → **카운팅 정렬**: `cnt[값]+=1` 후, `for v in range(10001): print(v) * cnt[v]`. 메모리/속도 주의.

### 정렬 응용(키 정렬/안정성)
- **25305 (커트라인)**: 내림차순 정렬 후 K번째 값.
- **2108 (통계학)**: 평균/중앙값/최빈값/범위.  
  - 평균: **반올림(소수 .5 올림)** → `Decimal`의 `ROUND_HALF_UP` 권장.  
  - 최빈값: 복수면 **두 번째로 작은 값**.  
  - 중앙값: 정렬 후 가운데. 범위: 최댓값-최솟값.
- **1427 (소트인사이드)**: 숫자를 문자열로 바꿔 **내림차순 정렬** 후 출력.
- **1181 (단어 정렬)**: **중복 제거** 후, `key=(len, 단어)`로 정렬.
- **10814 (나이순 정렬)**: **안정 정렬** 요구. `key=(나이)`만 주면 입력 순서가 유지됨.
- **11650 (좌표 정렬하기)**: `key=(x, y)`.
- **11651 (좌표 정렬하기 2)**: `key=(y, x)`.

### 탐색 (이진/집합)
- **1920 (수 찾기)**: 정렬 + 이진 탐색 또는 `set` membership (`x in s`).
- **10815 (숫자 카드)**: 여러 질의 → `set`이 간단/빠름. (이진 탐색도 연습해 보기)

### 파라메트릭 서치
- **2805 (나무 자르기)**: 위 예시 코드 참고. 시간복잡도 O(n log maxH).
- **2110 (공유기 설치)**: **최소 간격 d**를 이분으로 가정하고, 그 간격으로 라우터를 **탐욕적으로 배치** 가능한지 체크.
```python
def can_place(houses, C, dist):
    cnt = 1
    last = houses[0]
    for x in houses[1:]:
        if x - last >= dist:
            cnt += 1
            last = x
    return cnt >= C

def max_min_distance(houses, C):
    houses.sort()
    lo, hi = 1, houses[-1] - houses[0]
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_place(houses, C, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
```

---

## 6. 자주 발생하는 실수 체크리스트
- [ ] 대량 입력에서 `input()`을 그대로 사용 (→ `sys.stdin.readline` 사용)
- [ ] **카운팅 정렬**에서 출력 누락/순서 오류 (`for v in range(10001)` 고정)
- [ ] `2108`에서 반올림 방식 오류 (파이썬 `round`는 **banker’s rounding**)  
  → `Decimal` + `ROUND_HALF_UP` 사용 권장
- [ ] `10814`에서 안정 정렬 요구 간과 (동일 나이에 대해 입력 순서 유지)
- [ ] 파라메트릭 서치에서 조건식 부등호 반대로 작성함

---

## 7. 시간복잡도 미니 표
| 유형 | 알고리즘/연산 | 시간 |
|---|---|---|
| 정렬 | 버블/선택/삽입 | O(n²) |
|  | 퀵(평균)/병합/힙/TimSort | O(n log n) |
| 탐색 | 선형 탐색 | O(n) |
|  | 이진 탐색 | O(log n) |
| 파라메트릭 서치 | 조건 검증 × log(범위) | O(n log R) |

---

## 8. 연습 루틴(권장)
- Day 1: 기초 정렬 3종(버블·선택·삽입) 개념/손코딩 → 소형 데이터 테스트
- Day 2: 내장 정렬로 2750/2751/10989 해결 + 입출력 최적화 연습
- Day 3: 키 정렬/안정 정렬 문제(1181, 10814, 11650, 11651)
- Day 4: 이진 탐색(1920, 10815), 파라메트릭 서치(2805, 2110)
- Day 5: 복습 + 본인 언어로 개념 요약 정리

---

## 9. 미니 퀴즈 (정답은 토글 클릭)
1) 파이썬 정렬이 **안정적**이라는 의미는?  
2) `1181`처럼 길이→사전순 정렬은 `key=`에 어떤 튜플을 주면 될까?  
3) 이진 탐색을 쓰기 위한 **필수 전제**는?  
4) `10989`가 카운팅 정렬로 빠른 이유는 무엇 때문인가?  
5) `2110`에서 후보 거리 `d`가 주어졌을 때, 무엇을 어떻게 검사해야 할까?

<details>
<summary>정답 보기</summary>
1) 같은 키의 원소들이 정렬 후에도 **입력 순서를 유지**하는 것.  
2) `key=lambda w: (len(w), w)`  
3) **정렬된** 배열(또는 단조성 보장)  
4) 값의 **범위가 작고 고정**되어 빈도 카운트만으로 정렬이 가능해서.  
5) 집을 오름차순으로 보고, 간격이 `d` 이상이 되도록 **탐욕적으로 공유기 배치**가 가능한지 확인한다.
</details>

---

### 부록 A. 정렬/탐색 치트시트
```text
정렬 API
- list.sort(reverse=False, key=...)
- sorted(iterable, reverse=False, key=...)

힙
- import heapq; heappush(h, x); heappop(h)

이진 탐색(기초)
- while lo <= hi: mid=(lo+hi)//2
- if a[mid] < target: lo=mid+1 else: hi=mid-1

파라메트릭 서치
- 조건을 만족? → 더 큰/작은 쪽으로 범위 이동
- 최대값 찾기: 만족 시 lo=mid+1; 최소값 찾기: 만족 시 hi=mid-1
```

### 부록 B. 디버깅/출력 팁
```python
# 대량 출력 모으기
import sys
out = []
# ... append 문자열들
sys.stdout.write('\n'.join(out))
```


