### [ LeetCode ] 424. Longest Repeating Character Replacement

### 📌 문제 링크

[LeetCode - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

### ⚠️ 제약조건

- 1 <= s.length <= 105
- s consists of only uppercase English letters.
- 0 <= k <= s.length

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 먼저 left 를 움직이며, left 부터 끝까지 움직이며 문자열 s 의 범위를 설정하여 한번의 left 의 움직임의 루프 안에서 dictionary 를 설정하여 해당 범위의 문자열의 문자별 빈도를 저장한다. 여기서 left 부터 right 까지의 길이에 최대 빈도값을 빼주게 된다면 최소로 수정해서 가장 긴 동일한 연속된 문자를 만들 수 있는데, k 이하로만 설정되어야하니 조건문을 통하여 이를 벗어나게 된다면 continue 를 통하여 다음 left 주기로 넘어가게 해주었다. 하지만 Two Pointer 가 아닌 Bruteforce 방식에 가까운 풀이 때문일까 시간초과가 발생했다. 코드 개선을 진행해보자.

-   **접근 2**
  - 접근 1번의 풀이에서는 이중 for 문을 통하여 조회를 하게되면 O(N^2) 의 시간복잡도를 가지게 되었다. 그렇기에 k 의 조건이 벗어나게 되는 부분에서 continue 를 통한 다른 left 루프로 계속하는 대신, left 값을 직접 이동하며, 이동전에 dictionary 에서의 count 를 1 줄여주고 이동하며 O(N) 의 시간복잡도를 가지게 개선할 수 있었다.

### 📝 추후 개선점

- range 부분에서 어자피 left 가 0 부터 시작이라면 range 의 특성상 range(left, len(s)) 가 아닌, 관례상 range(len(s)) 로 사용하는 것이 더 직관적이며 일반적이다. 이러한 점을 잊지 말자.

### 💻 풀이 코드

```python
#풀이 1 (Bruteforce)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        for left in range(len(s)):
            count = {}
            for right in range(left, len(s)):
                count[s[right]] = count.get(s[right],0) + 1
                win_length = right - left

                max_count = count[max(count, key=count.get)]
                
                if(win_length + 1 - max_count <= k):
                    max_length = max(win_length + 1, max_length)
                else:
                    continue

        return max_length
```

```python
#풀이 2 (Sliding Window)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = {}

        for right in range(left, len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            win_length = right - left

            max_count = count[max(count, key=count.get)]
                
            if(win_length + 1 - max_count <= k):
                max_length = max(win_length + 1, max_length)
            else:
                count[s[left]] -= 1
                left += 1

        return max_length
```
