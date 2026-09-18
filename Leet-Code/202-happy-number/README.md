### [ LeetCode ] 202. Happy Number

### 📌 문제 링크

[LeetCode - Happy Number](https://leetcode.com/problems/happy-number/description/)

### ⚠️ 제약조건

- 1 <= n <= 231 - 1

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 반복을 통하여 한단계에 대한 숫자의 합을 계속 계산하고, Set 을 통하여 사용했던 Pair 에 다시 도달하면 무한 루프에 빠졌다고 판단하여 False 를 반환하는 간단한 로직을 사용했다. 이렇게 한다면 n 의 자리수의 개수는 log_10 n 에 비례하기에, O(log n) 의 시간복잡도를 가지며, 결국 같은 Combination 의 반복이 발생하기에 일정한 공간사용이 발생하여 O(1)의 공간복잡도를 가지게 된다.

### 📝 추후 개선점

- 생각보다 쉽게 풀었으며, 사실 이러한 반복과 Set 작업 없이도 수학적으로 깔끔하게 계산되는 트릭이 없나 오래 고민했었던 것 같다. 이런 점을 제외하면, Iteration 으로 푸는 과정에서 cal() 함수에서 str() 과 int() 를 사용하여 값의 타입을 지속적으로 변경 및 계산을 진행하고 있지만, 이를 개선하여 단순 수식적으로 계산할 수 있었겠다라고 생각했다.

### 💻 풀이 코드

```python
#풀이 1 (Iterative & Set)
class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num): 
            result = 0
            for digit in str(num):
                result += int(digit)*int(digit)
            return result

        visited = set()
        while(1):
            n = cal(n)

            if(n == 1):
                return True

            if(n in visited):
                print(n)
                return False
            else:
                visited.add(n)
```
