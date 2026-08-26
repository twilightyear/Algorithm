[ Image ]

### [ LeetCode ] - 15. 3Sum

### 📌 문제 링크

[LeetCode - 3Sum](https://leetcode.com/problems/3sum/description/)

### ⚠️ 제약조건

- 3 <= nums.length <= 3000
- -105 <= nums[i] <= 105

### 🛠️ 풀이 접근 및 분석

> Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

> Notice that the solution set must not contain duplicate triplets.

-   **접근 1**
  - i, j, k 를 통한 접근으로 구하면 어떨까? 라는 생각을 1초 정도 가지고 바로 쓰면 안되겠다는 생각을 했다. n 개의 요소를 가지는 arr 에 대하여 봤을때, 단순하게 겹치지 않게 i는 0부터, j는 i부터, k는 j 부터 본다고 가정하면, i와 j만 봐도 n(n-1)*1/2, 즉 O(N^2) 를 가지며, k 까지 고려하면 이는 가볍게 넘어선다. 대충 계산해봐도 O(N^3) 의 시간복잡도를 가지고, 이는 해결방법이 전혀 아닐 가능성이 높다. 본 알고리즘에 대한 코드를 작성할 가치도 없다고 판단하고 다른 접근법을 생각해보았다.

-   **접근 2**
  - 정렬 후 i 를 for 문으로 돌리되, 나머지 j 와 k 역할을 기존에 해왔던 전통적인 투포인터로 해결 가능하다고 생각했다. 하지만 이렇게 단순히 구현한다면 동일한 조합이 여러번 출력되는 현상이 발생할 수 있었으며, 이는 nums[i] 부분, nums[right] 부분, 마지막으로 nums[left] 부분에 대하여 각각 중복방지 로직을 작성할 필요가 있었다.

### 📝 추후 개선점

-  본 풀이는, sort 를 통하여 O(nlogn) 의 시간복잡도를 처음 가지게 되며, 이후 i 에 대한 for 문 안의 투 포인터의 시간복잡도는 O(N * N) 을 가지게 되니, 결국 총 O(N^2) 의 시간복잡도를 가지게 된다. 공간복잡도는 결과 반환용 arr 인 result_arrs 의 필요 길이가 N 이며, 이는 O(N) 의 공간복잡도를 가지게 한다. 위의 접근 2 에서 추가적으로 서술하지는 않았지만, 중복방지 코드를 작성하지 않은 코드로 테스트를 돌려보며 왜 안되지 라고 하며 고민을 조금 했었다. 오랜 고민의 시간을 가져도 해결이 안되어 도움을 받고자 코드를 찿아보니, 중복방지가 필요하다는 사실을 깨닫고 적용하는 과정이 필요했다. 이렇게 아직 접근 및 풀이에 대한 실력이 부족하다는 것을 느껴서 더욱 공부와 노력이 필요하다는 생각을 하게 되었던 문제였다.

### 💻 풀이 코드

```python
#풀이 1 (Two Pointer)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_arrs = []
        nums.sort()

        for i in range(0,len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i>0 and nums[i] == nums[i-1]: #nums[i] 에 대한 중복방지
                continue

            while(left<right):
                tsum = nums[left]+nums[right]+nums[i]

                if(tsum > 0):
                    right-=1
                elif(tsum < 0):
                    left+=1
                else:
                    result_arrs.append([nums[i],nums[left],nums[right]])

                    while(left<right and nums[left]==nums[left+1]): #nums[left] 에 대한 중복방지
                        left+=1
                    while(left<right and nums[right]==nums[right-1]): #nums[right] 에 대한 중복방지
                        right-=1
                    
                    right-=1
                    left+=1

        return result_arrs
```

### 🤔 고찰

-  사실 처음 보았을때 이전에 풀이했던 Two Sum 문제들이 떠올라 사실 Two Pointer 로 접근하면 정말 좋겠다라는 생각은 가지고 있었다. 하지만 막상 적용하려니 "Three Pointer" 도 만들어도 돼? 라는 생각과, 이를 어찌 구현을 해야할까라는 생각이 들었었다. 하지만 막상 조금 더 생각해보니 그렇게 복잡할것까지도 없었다. 단순히 그냥 i 를 for 문으로 돌리고 나머지 부분을 투포인터를 사용하면 되는 것이였다. 추후 개선점 부분에서도 동일한 내용을 서술하긴 했지만, 이렇게 알고리즘 문제 풀이 과정에 있어서 아직 부족함을 느꼈던 문제였다.
