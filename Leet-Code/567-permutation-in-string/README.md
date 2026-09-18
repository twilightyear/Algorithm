### [ LeetCode ] 567. Permutation in String

### 📌 문제 링크

[LeetCode - Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)

### ⚠️ 제약조건

- 1 <= s1.length, s2.length <= 104
- s1 and s2 consist of lowercase English letters.

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 두 s1 와 s2 에 대하여 Counter 을 이용하여 확인하는 로직을 구성했다. s1 가 s2 보다 긴 경우에서는 어떠한 것도 성립할 수 없이니 False 를 반환하게 하는 것으로 시작하여, Sliding Window 의 길이를 조작하며 Permutation 을 확인하는 방식으로 코드를 구성했지만 1083 ms 의 소요시간이 발생했다. 최악의 경우 두 s1 와 s2 의 길이 N 과 M 에 대하여 O(N) 의 공간복잡도와 O(N*M) 의 시간복잡도가 발생한다.
-   **접근 2**
  - s1 의 count 를 관리하는 알파벳 개수만 사용하는 배열 하나와 Sliding Window 에서의 개수를 관리하는 배열 하나를 만들어서 사용한다. 접근 1번과 마찬가지로 s1 와 s2 의 길이에 있어서 s1 가 더 길다면 False 를 반환하게 하는 것으로 시작한다. 여기서 먼저 s1 의 길이만큼, s1 를 조회하며 s1_c 에 알파벳 위치에 대한 인덱스에 개수를 더하고, 동시에 s1 의 길이만큼만 s2 를 조회하여 w_c 에 알파벳 위치에 대한 인덱스에 개수를 더한다. 여기서 만약 s1_c 와 w_c 가 같다면 현재 위치가 Permutation 이라고 할 수 있으니 True 를 반환하게 하며, 이외에는 추가 확인 과정을 위하여 for 문을 통하여 s1 까지 확인했다는 사실을 고려하여, s1의 길이부터 s2 의 길이까지를 Sliding window 를 통하여 위치를 조작해주며 이동한다. 여기서 매 이동마다 count 개수를 업데이트하고 Permutation 인지 확인하는 과정을 가진다. 끝나기 이전에 찿았다면 True 를 반환하지만, 찿지 못했다면 루프 밖에서 False 를 반환한다. 이렇게 코드를 구성하면 11 ms 의 소요시간이 발생하며, s2 의 길이 M 에 대하여 O(M) 의 시간복잡도와, 일정한 공간에 대하여 O(1) 의 공간복잡도를 가진다.
### 📝 추후 개선점

- Counter 로 개수를 관리해보겠다는 접근은 좋았지만, 다른 사람들의 풀이들을 참고해 보았을때 알파벳 개수만큼만의 배열 두개를 만들어서 훨씬 효율적이게 관리할 수 있다라는 아이디어가 있다라는 사실을 알게 되었다. 처음 Sliding Window 유형들을 풀때보다는 접근방식의 개선이 있었던것 같지만, 아직 더 배워야할 것이 많은 것 같다.

### 💻 풀이 코드

```python
# 풀이 1 (Sliding Window & Counter)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        left = 0
        right = len(s1) - 1

        if(len(s1) > len(s2)): #s1 가 s2 보다 긴 경우 바로 False 반환
            return False

        while(right<len(s2)): #Sliding Window 를 조작하며 Permutation 확인
            c2 = Counter(s2[left:right+1])

            if(c2 == c1):
                return True

            left+=1
            right+=1

        return False
```

```python
# 풀이 2 (Sliding Window & Array)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False

        s1_c = [0]*26
        w_c = [0]*26

        for char in range(l1):
            s1_c[ord(s1[char]) - ord('a')] += 1
            w_c[ord(s2[char]) - ord('a')] += 1

        if(s1_c == w_c):
            return True

        for i in range(l1, l2):

            w_c[ord(s2[i]) - ord('a')] += 1
            w_c[ord(s2[i-l1]) - ord('a')] -= 1

            if(s1_c == w_c):
                return True

        return False
```
