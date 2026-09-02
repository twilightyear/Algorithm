### [ LeetCode ] 704. Binary Search

### 📌 문제 링크

[LeetCode - Binary Search](https://leetcode.com/problems/binary-search/description/)

### ⚠️ 제약조건

- 1 <= nums.length <= 104
- -104 < nums[i], target < 104
- All the integers in nums are unique.
- nums is sorted in ascending order.

### 🛠️ 풀이 접근 및 분석

> Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

> You must write an algorithm with O(log n) runtime complexity.

-   **접근 1**
  - 문제에서는 O(log n) 의 시간복잡도를 가지는 Search 알고리즘을 원한다. 여기서는 전통적인 Bianry Search 알고리즘을 그대로 사용하면 그대로 적용이 가능 할 것이다. 

### 📝 추후 개선점

-  mid 의 계산 방식은 직관적이게 작성되었다. 하지만,

mid = (left+right) // 2

에서 만약 right 가 가르키는 부분이 표현가능한 최대 부분이면 어떻게 될 것인가? 오버플로우가 발생할 수 있는 경우를 고려하여, 동일한 표현법이지만, 이러한 문제가 발생하지 않는

mid = left + (right - left) // 2

해당 코드를 사용함으로써 잠재적인 문제를 해결할 수 있다.

물론 파이썬이라는 언어에서는 임의정밀로를 사용하기에 이러한 문제는 발생할 수 없다고 할 수 있다. 예리한 지적이다. 하지만 살면서 파이썬만 쓸 것이 아니기도 하고, 이러한 잠재적 문제점에 대한 공부는 필요하다고 생각한다.

### 💻 풀이 코드

```python
#풀이 1 (Binary Search)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1


        while (left<=right):
            mid = (left+right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1 # 찿지 못했을 경우 -1 반환
```

### 🤔 고찰

- 딱히 어려웠거나 고민을 했던 문제는 아니였다. 이제 전역까지 35일 정도 남았다. 전역 전까지 얼마나 더 실력이 늘지는 잘 모르겠지만, 꾸준히 열심히 해보자는 초심을 잃지 말자.
