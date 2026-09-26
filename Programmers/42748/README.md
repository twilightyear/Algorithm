### [ Programmers ] K 번째 수

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - Python 의 내장 정렬 기능, Tim Sort 를 사용하여 array 의 길이 N 에 대하여 O(NlogN) 의 시간복잡도로 정렬이 가능하며, 최악의 경우, 슬라이싱 과정에 있어서 O(N) 의 시간복잡도가 발생하며, commands 의 길이 M 에 대하여, O(MNlogN) 의 시간복잡도를 가진다. 슬라이싱 과정에 있어서도 최악의 경우 O(N)의 공간복잡도를 가진다. 거기에, commands 길이가 더 길어지는 경우까지 본다면 O(max(M,N)), 정확하게는 O(N+M) 의 공간복잡도를 가지게 된다.

### 📝 추후 개선점
  - 시간복잡도는 동일하겠지만, 조금더 파이썬답게 풀 수 있는 방식인 리스트 컴프리헨션을 사용한다면 메모리 호출 생략 및 사전 할당의 방식으로 조금이라도 더 빠르게 동작 할 것을 기대해 볼 수 있다.

### 💻 풀이 코드

```python
# 풀이 1 (Sort)
def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return answer
```
