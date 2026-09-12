### [ LeetCode ] 69. Sqrt(x)

### 📌 문제 링크

[LeetCode - Sqrt(x)](https://leetcode.com/problems/sqrtx/description/?envType=problem-list-v2&envId=binary-search)

### ⚠️ 제약조건

- 0 <= x <= 2^31 - 1

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 제약조건을 보면, 0 부터 2^31 -1 의 값에 대한 해답을 구하다보니, 단순 bruteforce 로 1 씩 조작하다보면 반드시 시간초과가 발생하게 될 것이라는 것을 알 수 있었다. 그렇기에, left 를 0 으로 잡고, right 를 x 로 잡아서 범위를 설정한 Binary Search 를 사용하여 구현이 가능했다.

### 📝 추후 개선점

- 사실 더욱 어려운 Binary Search 문제들을 풀어보려고 하다가, while 의 left 와 right 의 설정과 if 문에서 mid 값을 통한 비교과정 등에서 직관적인 풀이가 계속 안되는 것 같아서 이번에 Binary Search 에 있어서 다소 쉬운 문제를 찿아오게 되었다.. 앞으로도 더욱 구현관련해서의 충분한 이해가 있는 상태의 Binary Search 를 사용해야할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Binary Search)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while(left < right):
            mid = left + (right - left + 1) // 2
            power = mid*mid

            if(power < x):
                left = mid
            elif(power > x):
                right = mid - 1
            else:
                return mid

        return right
```
