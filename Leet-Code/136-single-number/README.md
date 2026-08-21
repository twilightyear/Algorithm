### [ LeetCode ] 136. Single Number

### 📌 문제 링크

[LeetCode - Single Number](https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array)

### ⚠️ 제약조건

- 1 <= nums.length <= 3 * 104
- -3 * 104 <= nums[i] <= 3 * 104
- Each element in the array appears twice except for one element which appears only once.

### 🛠️ 풀이 접근 및 분석

> Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

> You must implement a solution with a linear runtime complexity and use only constant extra space.

-   **접근 1**
    - 하나의 원소를 제외하고 전부 짝이 있다는 성질은 **bit** 연산을 활용하여 **xor** 처리하면 쉽게 처리 가능할 것이라고 판단했다. 값들을 전부 **xor** 연산하면, **0^A=A** 이며, **A^A=0** 인 성질이 활용되어 같은 값은 **0** 으로 변하고, 하나 남을 원소 **B** 에 **0** 과 **Xor** 되면 **B^0=B** , 즉 우리가 원하는 값 하나가 나오게 될 것이다.

### 📝 추후 개선점

-  사실 요소 **N** 개에 대하여 N번 계산해야하니 **O(N)** 의 시간복잡도를 가지며, **result** 값에 업데이트를 해 나가니 **O(1)** 의 공간복잡도를 가지는 매우 효율적인 풀이법이였다. 다만, 코드 변수명 설정에서 **item** 보다 **num** 으로 변수명을 설정하여 더욱 직관적인 변수명 설정을 지향해야겠다. 효율적인 풀이와 별도로 코드의 가독성과 직관적인 이해를 돕는 작성법도 물 흐르듯 익숙해져야한다.

### 💻 풀이 코드

```python
#풀이 1 (Xor)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for item in nums:
            result^=item #Xor 연산
        return result
```

### 🤔 고찰

- 사실 **Bit** 를 이용한 접근법은 알고리즘 자료들을 읽으며 우연하게 보았던 접근법이다. 이와 같은 접근법이 잘 떠올라서 적용한 것이 매우 뿌듯했다. 이렇게 사실, 알고리즘 공부와 접근법 최적화는 정말 오랜 시간 연습해야하는게 맞는 듯 하다. 요즘 **Sort** 관련 알고리즘을 중점으로 코드를 해석 및 이해하고 공부하는 시간을 가지고 있다. 이러한 공부속에서 찿아낸 지식들을 적용할 수 있는 **Sort** 문제들을 풀면서도 동일하게 좋은 접근법을 찿아내서 풀이를 할 수 있길 기대한다.
