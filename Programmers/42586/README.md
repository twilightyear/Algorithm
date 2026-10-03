### [ Programmers ] 기능개발

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  -  먼저, 몇일 걸리는지, 기능별로 계산을 하여 저장을 진행한다. 그리고 그래프의 위의 꼭짓점을 계산하는 느낌으로, Queue 을 사용하여 꼭짓점이 나오기 전까지의 항목을, 임시 배열에 추가해주며, 변곡점이 등장하면 result 에 임시 배열의 길이를 반환하고, 임시 배열을 초기화한다. 여기서 pop 은 필연적으로 처음에 등장하기에, 비교할때 사용되었던 가장 최근 원소는 초기화 하는 과정에서 들어가줘야한다. 이렇게 구현한다면, O(N) 의 공간복잡도와 O(N) 의 시간복잡도를 가지게 된다.

### 📝 추후 개선점
  - 다른 사람들의 풀이를 살펴보니 zip 을 사용하여 기능의 작업률과 속도를 한번에 빠르게 계산하는 것을 포함하여 큐 안에 배열을 집어넣어 더욱 간결하게 코드를 구성한 것을 확인할 수 있었다. 이외에도, 내 코드와 달리, 변수만 사용하여 코드를 구성한다면 공간복잡도를 O(1) 로 개선할 수 있는 방안이 존재했다.

### 💻 풀이 코드

```python
#풀이 1 (Queue)

from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    result = []
    s = []
    
    for i in range(len(progresses)): #몇 일 걸리는지 기능별로 계산
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    while days:
        day = days.popleft()
        if s:
            if s[0] >= day:
                s.append(day)
            else:
                result.append(len(s))
                s = [day]
        else:
            s.append(day)
    
    if s:
        result.append(len(s))
        
    return result
```
