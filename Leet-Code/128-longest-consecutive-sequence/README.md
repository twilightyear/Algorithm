### [ LeetCode ] 128. Longest Consecutive Sequence

### 📌 문제 링크

[LeetCode - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

### ⚠️ 제약조건

- **0 <= nums.length <= 105**
- **-109 <= nums[i] <= 109**

### 🛠️ 풀이 접근 및 분석

> **Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.**

> **You must write an algorithm that runs in O(n) time.**

-   **접근 1**
  - 문제에서는 **O(N)** 의 시간복잡도 내로 풀기를 원하고 있다. 매우 곤란하다. 바로 떠오른 풀이법이 정렬 후 연속된 값 탐색이라는 그림을 그리고 있었지만, 정렬을 해버리면 좋은 정렬 알고리즘을 적용해도 평균적으로는 **O(NlogN)** 의 시간복잡도를 가지게 될 것이다. 그렇기에 **Set** 을 사용하는 방식을 적용했다. **Set** 을 이용하면 중복요소때문에 소요될 수 있는 잠재적 시간낭비를 포함한 여러 이점을 얻을 수 있으며, 무엇보다 **sort** 와 다르게, 추출한 값에 대하여 그 값에 연속적인 값이 있는지 확인하기 위하여 **Hash map** 방식으로 **O(1)** 의 시간복잡도로 조회가 가능하다는 특징때문에 문제 풀이에 매우 효율적일 것이다.

### 📝 추후 개선점

-  사실 문제 풀이에 매우 시간 소요가 컸다. **Sort** 라는 방식을 사용한다는 방식에 시간도 걸렸다. **N** 개의 요소가 전부 다른 최악의 경우에서 N 번의 아이템 추출과, 이에 따른 아이템에 이어지는 값이 있는지 확인하는 **Hash map** 을 이용한 검증이라는 방식을 떠올리기가 상당히 소요되었다. 게다가 이것 뿐만이 아니라, 아이템 추출 과정에서 **Set** 에서 보는 것이 아니라. **raw** 한 **nums** 리스트에서 값을 꺼내는 형식의 코드로 최초구성한지라, 시간초과와 같은 문제가 발생했다. 솔직히 말하자면 본 문제같은 경우는 어떤 방식이 좋은지 꼬아서 나온 것이 아닌 정말 기본 유형의 알고리즘 문제라고 생각한다. 접근 방식에 있어서 정말 연습이 더 필요할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Set)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest=0

        for num in nums_set:
            if num-1 not in nums_set: #num 보다 1 작은, 즉 num이 연속적 부분의 첫 값 후보로 설정한다.
                length = 1
                while num+length in nums_set: #뒤에 연속적 값이 계속 나오면 length 를 증가시킨다.
                    length+=1
                
                longest = max(length,longest) #값 최신화

        return longest
```

### 🤔 고찰

- 추후 개선점 부분에서도 말했지만, 직관적이지 않고 어려운 알고리즘 문제에 도전하려면 정말 탄탄한 기본기가 필요하다고 생각한다. 그러한 수준을 목표로 공부를 하는 만큼, 이번처럼 문제를 풀면서 잘못된 접근방법, 더 나아가 좋은 접근방법을 택하여 나아갔지만 이상한 부분에서 문제가 발생하는 경우를 줄여야 하는것은 정말 필요할 것이다.
