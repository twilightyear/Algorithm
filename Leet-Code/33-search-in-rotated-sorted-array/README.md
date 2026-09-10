### [ LeetCode ] 33. Search in Rotated Sorted Array


### 📌 문제 링크

[LeetCode - Search in Rotated Sorted Array
](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

### ⚠️ 제약조건

- 1 <= nums.length <= 5000
- -104 <= nums[i] <= 104
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -104 <= target <= 104

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 문제는 O(logn) 의 시간복잡도를 가지게 풀기를 원한다. 바로 생각난 풀이는 Binary Search 를 통하여 가장 작은 값의 인덱스를 구하는 것이다. 이 인덱스와 target 값을 바탕으로 left 와 right 를 적절하게 지정하여 다시 Binary Search 를 하게 된다면 O(2logn), 상수항을 무시하면 O(logn) 이 되게 된다.

### 📝 추후 개선점

- 다른사람들의 풀이를 살펴보니, 내가 했던 두번의 Binary Search 구조가 아닌, 한번의 Binary Search 를 통하여서도 답을 구한 것을 확인할 수 있었다. 
아래처럼, mid 를 기준으로 왼쪽 구간이랑 오른쪽 구간의 정렬 여부를 확인하고, 정렬이 되어있다면 해당 범위 안에 target 값이 있는지 확인하고 있다면 그 범위로 left 와 right 를 좁힌다. 아니라면 그 구간에 없다는 것이니 left 와 right 를 사용하여 구간을 배제한다. 이러한 풀이법처럼 너무 복잡하게 풀지 않고 간결한 풀이를 할 수 있는 역량을 길러야겠다.


```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = left + (right - left) // 2

            if(target == nums[mid]):
                return mid

            if(nums[left] <= nums[mid]): #왼쪽 구간이 정렬되어 있는 경우
                if(nums[left] <= target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            elif(nums[mid] <= nums[right]): #오른쪽 구간이 정렬되어 있는경우
                if(nums[mid] < target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
            
            
        return -1
```



### 💻 풀이 코드

```python
# 풀이 1 (Binary Search)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        #최소값의 index 탐색
        while(left < right):

            min_idx = left + (right - left) // 2
            if(nums[min_idx] > nums[right]):
                left = min_idx + 1
            else:
                right = min_idx

        pivot = left

        #범위에 따라 left right 값 설정
        if pivot == 0: #만약 단순 정렬된 형태라면
            left = 0
            right = len(nums)-1
        elif nums[pivot] <= target and target <= nums[-1]: #최소값 <= target <= 마지막원소 이라면
            left = pivot
            right = len(nums)-1
        else:
            left = 0
            right = pivot-1

        #다시 Binary Search
        while(left <= right):
            mid = left + (right - left) // 2

            if(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] == target):
                return mid
            
        return -1
```

### 🤔 고찰

- 이제 전역까지 얼마 안남은 것 같다. 이제 전역하고 여러 활동들도 하면서 되게 할 것들이 많다는 생각에 스트레스도 많이 받는 것 같다. 하지만 꾸준히 하며 기초 체력을 지금 길러둬야 더욱 의미있게 공부와 활동들을 할 수 있는 것 아니겠는가. 더 열심히 화이팅 해보자.
