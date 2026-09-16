### [ LeetCode ] 3. Longest Substring Without Repeating Characters

### 📌 문제 링크

[LeetCode - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

### ⚠️ 제약조건

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 문자열 s 의 문자들을 right 로 순회한다. 여기서 현재 순회중인 char 에 대하여 이미 Hashmap 에 존재하거나, 현재 Window 안에 Hashmap 을 통하여 현재 right 값들의 조회 과정에서 가장 마지막으로 등장했던 인덱스를 저장한다. 만약 right 의 조회과정에서 가장 마지막 해당 값이 등장했으며, 현재 window 안에 있으면 left 값을 이전에 등장했던 인덱스 다음으로 옮겨서 window 를 재조정한다. 이와같은 상황에서 매 right 루프마다 window size를 max length 에 최신화 하는 것으로 중복없는 가장 긴 부분 문자열을 구할 수 있다. 이렇게 한다면 최악의 경우 O(N)의 공간복잡도를 가지지만 O(N) 의 시간복잡도를 가지게 할 수 있다.

### 📝 추후 개선점

- 사실 최초 접근은 문자의 가장 마지막 인덱스를 Hashmap 에 저장하는 것이 아닌, 문자의 등장 횟수를 저장하여 조회를 했다. 분명 문제를 풀 수 있는 방식이면서 시간복잡도도 O(N) 으로 동일하게 풀 수 있지만, 상수 시간에서 분명히 불리한 방식이였다. 이렇게 동일한 문제에 풀 수 있는 여러가지 방법들을 고루 익히며, 가장 적절한 방식을 선택하여 풀 수 있는 역량을 더 길어야 할 것 같다.

### 💻 풀이 코드

```python
#풀이 1 (Sliding Window & Hashmap)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_index = {}

        for right in range(len(s)):
            current_char = s[right]

            if current_char in last_index and last_index[current_char] >= left:
                left = last_index[current_char] + 1

            last_index[current_char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
```
