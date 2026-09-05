### [ LeetCode ] 153. Find Minimum in Rotated Sorted Array

### 📌 문제 링크

[LeetCode - Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

### ⚠️ 제약조건

- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.

### 🛠️ 풀이 접근 및 분석

> Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

> [4,5,6,7,0,1,2] if it was rotated 4 times.
> [0,1,2,4,5,6,7] if it was rotated 7 times.
> Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

>Given the sorted rotated array nums of unique elements, return the minimum element of this array.

> You must write an algorithm that runs in O(log n) time.

-   **접근 1**
  - 문제 앞부분만 보고 바로 sort 이후 첫번째 원소를 출력하면 되지 않나? 라는 생각에 구상을 하고 있었지만, 문제 마지막 부분에서 O(log n) 의 시간복잡도를 제약조건으로 걸었다. 이는 sort 의 시간복잡도가 O(nlogn) 이라, 사용이 불가능하다. 그래도 한번 구상한 코드는 돌려보고 싶어서 돌렸는데 시간 통과가 나오긴 했다. 하지만 문제에서 걸었던 제약조건에 위배되니 다른 접근 방식을 사용할 필요가 있었다.

-   **접근 2**
  - 문제에서 주어진 시간복잡도인 O(logn) 을 볼 수도 있으며, 또한 이미 정렬된 배열에 대하여 값을 shift 했다는 문제 특성상, Binary Search 의 적용을 의도한 문제라는 것을 알 수 있었다. 먼저 right 값이 mid 값보다 작다면, 기존 배열의 마지막과 시작 부분이 포함된 영역임을 알 수 있다. 그러므로, mid+1 부터 right 까지의 영역 안에 가장 작은 값이 있음을 유추할 수 있다. 그렇기에, left 값을 mid+1 로 설정해준다. 이 경우가 아니라면, 즉 right 값이 mid 값보다 큰 경우에는, mid 를 포함해서 더 아래쪽에 위치한다. 그렇기에 right 값을 mid 로 바꿔주면 될 것이다. 여기서 핵심은 mid -1 를 하게되면, 만약 mid 가 답일 경우 찿을 수 없다는 점을 파악하는 것이였다.

### 📝 추후 개선점

-  사실 문제의 요구사항과 출제자의 의도라고 하면 파악을 했던 것 같다. 하지만 구현에 있어서 사실상 크게 어려움을 겪었던 문제였다. 문제를 더 잘 파악해서 조건문 설정을 하고 이를 통하여 깔끔하게 문제를 풀 수 있는 역량을 길러야할 것이다.

### 💻 풀이 코드

```python
# 풀이 1 (Sort)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()

        return nums[0]
```

```python
# 풀이 2 (Binary Search)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left<right):
            mid = left + (right - left) // 2

            if(nums[mid] > nums[right]): # 중간값인 mid 가 오른쪽보다 크다면 논리적으로 최솟값은 여기 사이에 존재함.
                left = mid + 1
            else: #중간값인 mid 가 오른쪽보다 작다면, 최솟값은 mid 이거나, 더 아래에 있음
                right = mid

        return nums[right]
```

### 🤔 고찰

- 위에서도 언급했던 내용이지만, 문제의 요구사항은 파악했지만 세세한 논리적 구현에 있어서 어려움을 느꼈던 문제였다. 뭔가 너무 답답한 심정이 컸던것 같다. 이러한 구현력은 결국 꾸준한 문제풀이를 통하여 길러지는 역량이라고 생각한다. 앞으로의 시간이 적다고 하면 적으면서도, 넉넉하다고 하면 넉넉하다고도 할 수 있다고 생각한다. 지금 하는 이러한 연습이 실력을 형성하여 큰 도움이 될 것이라고 믿고있다.
