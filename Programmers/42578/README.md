### [ Programmers ] 의상

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - Default Dict 을 통하여 의상 종류별로 따로 리스트로 두어 저장한 후, 저장된 종류별 길이에 1 을 더하여 해당 종류를 안입고 있는 상태로 가정하여 모두 곱해준다. 하지만 알몸인 상태에 해당하는 경우는 제외해야하니 마지막에 1 을 빼주면 된다. 이렇게 한다면 의상 카테고리 종류의 개수 N 과 가장 많은 카테고리내 의상 개수인 M 에 대하여 최악의 경우 O(N*M) 의 공간복잡도와 시간복잡도를 가진다.

### 📝 추후 개선점

  - 사실 본 문제는 카테고리 내의 cloth 값은 크게 중요하지 않아 category 별로 그냥 list 가 아닌 int 로 값을 증가시켜 Counter 의 역할로만 사용한다면 카테고리 종류의 개수 N 에 대하여 O(N) 의 시간복잡도를 가지도록 코드를 개선할 수 있었다.

### 💻 풀이 코드

```python
# 풀이 1 (Hashmap)
from collections import defaultdict

def solution(clothes):
    map = defaultdict(list)
    
    for cloth, category in clothes:
        map[category].append(cloth)
        
    answer=1
    for item in map:
        answer*=(len(map[item])+1)
        
    return answer-1
```
