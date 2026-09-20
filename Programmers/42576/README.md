### [ Programmers ] 완주하지 못한 선수

[Programmers - 완주하지 못한 선수]


### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - Hashmap 을 사용한 풀이방식을 선택했다. 처음에 Set 을 사용해서 직관적으로 풀어볼까 생각했지만, 문제에서 동명이인이 있을 수 있다는 조건을 보고, Hashmap 이 적절하겠다고 생각했다. N 개의 참가자 이름에 있어서 최악의 경우 O(N) 의 공간복잡도와 O(N) 의 시간복잡도를 가지게 된다.

### 📝 추후 개선점

- 다른 사람들의 풀이를 살펴보니 단순 Counter 를 이용하여 a.Counter - b.Counter 처럼 계산을 하여 key 값을 통한 값 조회로 단 2줄만에 깔끔하고 빠르게 답을 얻어낸 것을 볼 수 있었다. 이렇게도 풀 수 있다니 참 신기할 따름이다.

### 💻 풀이 코드

```python
# 풀이 1 (Hashmap)
from collections import defaultdict

def solution(participant, completion):
    m = defaultdict(int)
    answer = ""
    for person in completion:
        m[person] += 1
        
    for person in participant:
        if m[person] == 0:
            return person
        m[person] -= 1
```
