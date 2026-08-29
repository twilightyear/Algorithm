### [ LeetCode ] 739. Daily Temperatures

### 📌 문제 링크

[LeetCode - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)

### ⚠️ 제약조건

- 1 <= temperatures.length <= 105
- 30 <= temperatures[i] <= 100

### 🛠️ 풀이 접근 및 분석

> Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

-   **접근 1**
  - 풀이 접근 방식에 있어서 일단 구현을 해보며 생각해보기로 생각하고 Bruteforce 로 구현해보았다. 역시나 최악의 경우 O(n^2) 의 시간복잡도를 가지며, 애초에 시간초과로 통과 조차 불가능했다. 다른 풀이 방법이 필요하다.

-   **접근 2**
  - Stack 을 사용해보려 했으나, 생각을 해본 여러 구성방법을 적용해도 O(n^2) 의 틀에서 벗어나기 힘들었다. 시간이 너무 걸려 다른 사람들의 풀이를 살펴보니 Stack 을 사용하지만 상당히 효율적인 작동방식의 코드가 존재했다.
  - 본 코드는 현재값을 기준으로 왼쪽부분을 바라보며, 그 부분이 작은 경우에 왼쪽으로 전진하며 result 라는 애초에 길이가 설정된 arr 에 대하여 값을 계속 최신화해주는 원리로 작동한다.
  - for 문 내부의 while 문으로 작동하기에 O(n^2) 일것같지만, 실제 연산 횟수를 보면 push 와 pop 연산을 합쳐서 최대 2n 번 작동하기에, 최악의 경우, O(n) 의 시간복잡도를 가진다고 할수 있다. 하지만 별도의 배열 사용하기에 O(n) 의 공간복잡도를 가진다.

### 📝 추후 개선점

-  접근 1번에 대한 시간복잡도를 분석하며 O(n^2) 가 아닌 O(n) 인 이유가 뭐인지 이해하는데 많은 시간이 소요되었다. 이는 분할상환분석 이라는 개념이 적용된 내용이다. 예시를 들자면 vector 에서 매우매우 가끔 발생하는 더블링 현상 때문에 값을 추가하는 함수의 시간복잡도가 O(1) 가 아닌 O(n) 라고 하지 않는 것 처럼 이러한 방식으로 해석이 있다는 사실을 기억해야 할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Bruteforce)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            found=False
            
            for j in range(i,len(temperatures)):
                if(temperatures[j]>temperatures[i]): #처음 커지는 값을 만나면 해당 값 추가
                    result.append(j-i)
                    found=True
                    break

            if not found:
                result.append(0) #못찿았다면 0 추가
        
        return result
```

```python
#풀이 2 (Stack)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
```

### 🤔 고찰

- 본 문제는 내림차순 모노톤 스택 패턴이 적용된 문제이다. 스택에 원소를 넣을때, 특정 정렬상태를 깨는 상황이 발생하면 기존 원소를 pop 해버리면서 기존 규칙을 유지하는 패턴의 양상을 보인다. 이러한 유형의 패턴은 추후 문제에서도 충분히 적용되어 다시 등장할 수 있으니 잊지 말고 기억해두자.
