### [ LeetCode ] 167. Two Sum II - Input Array Is Sorted

### 📌 문제 링크

[LeetCode - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

### ⚠️ 제약조건

- 2 <= numbers.length <= 3 * 104
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

### 🛠️ 풀이 접근 및 분석

> Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

> Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

> The tests are generated such that there is exactly one solution. You may not use the same element twice.

> Your solution must use only constant extra space.

-   **접근 1**
    > **Your solution must use only constant extra space.**
    - 이 조건 때문에 이전 **Two Sum** 문제에서 풀이한 방식인 **2차원 배열** 만들기를 통한 풀이는 불가능하다. 그렇기에 기존 주어진 배열만 사용해서 문제를 해결해야한다. 모든 요소에 대하여 **target** 을 뺀 값을 가지고 배열에 있는지 확인 및 인덱스 확인을 하면 일단 해결이 가능하다. 다만 **target** 을 뺀 값을 구하는것까진 빠르고 좋지만, 이 뺀 값의 인덱스 확인 과정에 있어서 전체조회 한번이 소요된다는 것이 매우 효율을 낮춘다. 코드를 분석해보았을때 제약사항을 수행하였으니 **O(1)** 의 공간복잡도를 가지나, **O(N^2)** 의 시간복잡도를 가진다. 실제로도 5359ms 라는 매우 두려운 시간소요가 있었다. 최적화나 다른 풀이법을 생각해봐야 겠다.

-   **접근 2**
    - 최적화를 고민해보기도 전에 **Two Pointer** 풀이는 어떤가 싶어서 바로 풀이해보았다. 문제에서 제약사항으로 걸어둔 공간 소모도 일정하며, 정렬되어있다는 특성상 **left=0 right=length-1** 로 설정하고 값이 크다면 **right** 를 **1** 줄이고, 크다면 **left** 를 **1** 크게 하여 접근한다면, 정답이 무조건 **1** 개 있다는 문제 특성상 무조건 정답이 도출되게 되어 있을 것이다. 이렇게 한다면 최악의 경우에도 **N** 개의 요소를 가지는 배열을 전부 조회하게 됨으로 **O(N)** 의 시간복잡도를 가지게 된다.

### 📝 추후 개선점

-  최초 풀이가 정말 잘못된 접근방식이였다. 다시 생각해보면 매우 아쉽다. 투포인터 라는 방식만 옮은 때에 떠올렸다면 매우 빠르고 정확하게 풀이가 가능했을 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Subtraction)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num_idx in range(len(numbers)):
            sub = target-numbers[num_idx] #뺀 값 구하기
            if sub in numbers:
                sub_idx = 0
                for j in range(len(numbers)): #뺀 값의 인덱스 확인 과정
                    if numbers[j] == sub:
                        sub_idx = j
                return [num_idx+1, sub_idx+1] #각각 1을 더한값을 반환
```

```python
#풀이 2 (Two Pointer)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 #투포인터 설정
        right = len(numbers)-1

        while(left<right):
            sum_tmp = numbers[left]+numbers[right]
            if(sum_tmp > target):
                right-=1
            elif(sum_tmp < target):
                left+=1
            else:
                return [left+1,right+1] #반환
```

### 🤔 고찰

- 생각보다 너무 멍청하게 풀었던 것 같다. 정렬되어있다라는 특성을 어떻게 활용할지 고민하며 **for** 문을 통한 순회와 그 과정에서 순회 내부에서 추가 인덱스 증감을 통하여 풀이하는 것에 너무 매몰되어 유연하게 풀이가 되지 않았던 것이 매우 아쉽다.
