# 4주차 자료 — 그래프 탐색 (BFS & DFS)

> 주제
>
> -   그래프 탐색: BFS(너비 우선 탐색), DFS(깊이 우선 탐색)
> -   그래프 표현: 인접 행렬, 인접 리스트
> -   BFS, DFS 구현 및 활용
>
> 목표
> -   **BFS와 DFS의 작동 원리 및 차이점**을 이해하고, 문제에 따라 적절한
    탐색 방법을 선택한다.
> -   인접 리스트와 인접 행렬의 장단점을 파악하고, 주어진 문제에 효율적인
    그래프 표현 방식을 결정한다.
> -   백준 실습을 통해 **재귀/스택(DFS)과 큐(BFS)**를 활용한 탐색 코드를
    능숙하게 작성한다.

---

## 1. 그래프 표현 방식 한눈에 보기

| 방식         | 아이디어                     | 장점                        | 단점                                    |
| ---------- | ------------------------ | ------------------------- | ------------------------------------- |
| **인접 행렬**  | 2차원 배열 `adj[u][v]`       | 구현이 직관적. 간선 존재 여부 O(1)    | 간선이 적은 그래프에서는 메모리 낭비 O(V²)            |
| **인접 리스트** | 각 정점에 연결된 정점 목록 `adj[u]` | 공간 효율적 O(V+E). 희소 그래프에 유리 | 간선 존재 여부 확인 O(degree(v)). 구현이 조금 더 복잡 |


### 1-1. 그래프 탐색 알고리즘 상세 & 예제

#### A) DFS (Depth-First Search)

-   **아이디어**: 한 정점에서 **깊게 들어가며** 탐색하다가 더 이상 갈
    곳이 없으면 되돌아와(백트래킹) 다른 경로 탐색.
-   **복잡도**: O(V+E)
-   **성질**: 스택 자료구조 또는 재귀 함수로 구현.
-   **활용**: 모든 정점 방문, 경로 존재 여부 확인, 사이클 탐색 등.

``` python
# 재귀 DFS
def dfs_recursive(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)

# 예시
# graph = {1:[2,3],2:[1,4,5],3:[1,6],4:[2],5:[2],6:[3]}
# visited = [False]*7
# dfs_recursive(graph, 1, visited) # 1 2 4 5 3 6
```

#### B) BFS (Breadth-First Search)

-   **아이디어**: 시작 정점에서 가까운 정점부터 차례로 탐색.
-   **복잡도**: O(V+E)
-   **성질**: 큐 자료구조로 구현.
-   **활용**: 최단 경로(간선 수 기준), 미로 탐색, 단계적 탐색.

``` python
# 큐 BFS
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 예시
# graph = {1:[2,3],2:[1,4,5],3:[1,6],4:[2],5:[2],6:[3]}
# visited = [False]*7
# bfs(graph, 1, visited) # 1 2 3 4 5 6
```

---


## 2. 필수 문제 (백준)

### 2-1. DFS/BFS 기본

-   **1260**: DFS와 BFS
-   **2606**: 바이러스
-   **11724**: 연결 요소의 개수

### 2-2. 최단 거리 / 탐색 응용

-   **2178**: 미로 탐색
-   **1697**: 숨바꼭질
-   **13549**: 숨바꼭질 3
-   **12851**: 숨바꼭질 2

### 2-3. 2D 배열 기반 탐색 (Flood Fill, BFS)

-   **1012**: 유기농 배추
-   **2667**: 단지번호붙이기
-   **7576**: 토마토
-   **7569**: 토마토 (3D)

---

## 3. 자주 발생하는 실수 체크리스트

-   [ ] **`visited` 배열 누락** → 무한 루프 가능.
-   [ ] **재귀 깊이 초과** → 파이썬 기본 제한(약 1000) 초과 시 런타임
    에러. 필요 시 `sys.setrecursionlimit()` 설정.
-   [ ] **`list.pop(0)` 사용** → BFS에서 시간 초과 위험.
    `deque.popleft()` 사용.
-   [ ] **단절 그래프 미처리** → 전체 탐색 시 모든 정점에 대해 DFS/BFS
    실행 필요.

---

## 4. 시간복잡도 요약

| 유형     | 알고리즘/연산  | 시간           |
| ------ | -------- | ------------ |
| 그래프 탐색 | BFS, DFS | O(V+E)       |
| 간선 조회  | 인접 행렬    | O(1)         |
|        | 인접 리스트   | O(degree(v)) |


---

## 5. 연습 루틴

-   **Day 1**: BFS/DFS 개념 이해.
-   **Day 2**: 1260, 2606 풀기 (재귀/큐 구현).
-   **Day 3**: 1012, 2667 (2D 배열 탐색).
-   **Day 4**: 1697, 7576 (최단 거리 BFS).
-   **Day 5**: 13549, 12851 (심화 문제 + 복습).

---

## 6. 미니 퀴즈

1.  DFS와 BFS 중 **최단 경로**를 보장하는 알고리즘은?
2.  인접 리스트와 인접 행렬 중 **메모리 효율성**이 더 좋은 방식은?
3.  DFS 재귀에서 `visited` 배열을 쓰지 않으면 어떤 문제가 발생하는가?
4.  그래프 탐색 알고리즘이 O(V+E)인 이유는?
5.  큐 BFS와 스택 DFS의 가장 큰 차이점은?

<details> <summary>정답</summary>

1. BFS
2. 인접 리스트
3. 같은 정점을 여러 번 방문 → 무한 루프 발생
4. 모든 정점 V와 간선 E를 한 번씩 확인하기 때문
5. BFS는 FIFO(가까운 정점 우선), DFS는 LIFO(깊은 정점 우선)

</details>

---

## 부록 A. DFS/BFS 치트시트

``` python
# DFS
def dfs_recursive(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)

# BFS
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
```
