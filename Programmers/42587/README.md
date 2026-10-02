### [ Programmers ] 프로세스

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 처음에는 heapq 를 사용하여 구현을 시도했지만, 실패시 가장 뒤의 큐에 추가한다라는 조건때문에 구현에 차질이 생기자, 문제에서 제공한 로직을 그대로 Queue 를 사용하여 구현했다. location 에 대한 확인이 필요하기에, tuple 을 사용하여 queue 에 (우선순위, 기존인덱스) 로 저장을 했다. 이 queue에서, 순서대로 앞에서 하나 pop 을 하고, queue 에 해당 값보다 우선순위가 큰 것이 있다면 queue 에 다시 append 로 추가해주며, 없다면 count 를 1 증가하고, 혹시나 여기서 tuple 의 뒷자리, 즉 기존 인덱스가 우리가 원하는 location 값과 같다면 누적한 count 값을 반환하도록 했다.

### 📝 추후 개선점
  - 현재 코드에서 any 라는 기능을 썼는데, 원래는 while 안의 for 문으로 구성하려다가, 참고자료를 보고 일부러 수정을 해보았다. 이렇게, 파이썬 다우면서도 가독성을 해치지 않는 표현 방식에 익숙해질 필요가 있을 것 같다. 또한, 앞서 언급했듯, 우선순위를 구해야하는 아이디어에 가로막혀, 단순 queue 로도 쉽게 풀이가 가능한 문제를 heapq 로 풀려고 너무 매몰되어 있었던 것 같다. 다양한 문제 풀이를 통한 경험을 통하여 아직 배울 것이 너무 많다.

### 💻 풀이 코드

```python
# 풀이 1 (Queue)
from collections import deque

def solution(priorities, location):
    queue = deque([(p,i) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        proc = queue.popleft()
        
        if any(proc[0] < q[0] for q in queue):
            queue.append(proc)
        else:
            count += 1
            if proc[1] == location:
                return count
```
