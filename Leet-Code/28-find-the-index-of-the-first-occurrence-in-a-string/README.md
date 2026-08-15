### [ LeetCode ] 28. Find the Index of the First Occurrence in a String

### 📌 문제 링크

[LeetCode - Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=two-pointers)

### ⚠️ 제약조건

- **1 <= haystack.length, needle.length <= 104**
- **haystack and needle consist of only lowercase English characters.**

### 🛠️ 풀이 접근 및 분석

> **Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.**

-   **접근 1**
    - 문제는 매우 단순하다. 문자열 **needle** 이 문자열 **haystack** 내부에서 처음 등장하는 인덱스를 반환하며, 없을경우 **-1** 를 반환하면 되는 문제이다. 가장 처음 떠오른 접근 방법은 **Two Pointer** 방식 중에서도 **Sliding Window** 방식이였다. 문자열 **needle** 의 길이만큼의 **window** 길이를 설정하여 움직이고, 이동 과정에서 동일한 문자열을 만나게 된 경우 **window** 의 왼쪽 포인터를 반환하면 될 것이다.

### 📝 추후 개선점

-  코드에서 **haystack==needle** 같은 경우는 빠르게 제외하도록 넣었지만 사실상 메인 로직 부분에서 다시한번 검출이 진행됨으로 결국 의미없는 부분이 되었다. 이러한 테스트 케이스에 대한 예비 검출도 중요하지만, 메인 로직에서 걸러주는 기능이 있다는 사실을 망각하여 효율을 낮추는 행위는 향후에 조심해야 할 것이다.

### 💻 풀이 코드

```
#풀이 1 (Sliding Window)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if(haystack==needle):
            return 0

        needle_length = len(needle)
        for i in range(0,len(haystack)-needle_length+1):
            if haystack[i:i+needle_length] == needle:
                return i


        return -1
```

### 🤔 고찰

- 항상 느끼는 것이 군대에서 무언가를 꾸준히 투자하며 공부한다는 것이 상당히 힘겹다는 사실이다. 최근들에서 뭔가 계속 바빠진 일상 때문에 항상 어느정도 공부하고 싶었던 분량만큼은 항상 채우지 못했던 것이 살짝 아쉬웠던 것 같다. 그래도 지금 공부에 **100%** 투자할 수 없는 상황인 경우에서는 결국 꾸준함과 끈기가 중요하다고 생각한다.
