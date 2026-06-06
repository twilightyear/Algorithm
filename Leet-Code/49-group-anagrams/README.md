

---


# [LeetCode] 49. Group Anagrams


---


### 📌 문제 링크
[LeetCode - Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)


---

### ⚠️ 제약조건
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.



---


### 🛠️ 풀이 접근 및 핵심 로직
- Hashmap을 사용하면 쉽게 문제를 해결 할 수 있다. 먼저 리스트에서 단어 단위로 추출을 하고 난 후에 단어마다 알파벳 단위로 재정렬을 시행한다. 이후에 정렬된 단어를 hashmap을 통하여 동일한 정렬된 단어에 해당하는 리스트에 원본값들을 추가해 나간다. 이후에 최종적으로 hash에서 value들만 list로 바꾸어서 반환하면 되었다.
---


### 📊 복잡도 분석
**시간복잡도**
- 단어들을 뽑아내는 for문에서 단어의 개수 N에 해당하는 O(N)의 시간복잡도를 가질것이며, 재정렬 과정에서 Tim Sort를 사용하는 파이썬 내장 정렬 원리상, 단어의 길이 L에 해당하는 O(LlogL)의 시간복잡도를 지닐것이다. Hashmap에 단어를 넣는 과정은 O(1)의 시간복잡도를 가질것이며, append 또한 O(1)의 시간복잡도를 가진다. 하지만 마지막으로 hash의 values를 뽑아내는 과정은 결국 O(N)의 시간복잡도를 가지며 list로 다시 변환하는 과정은 독립적으로 O(N)의 시간복잡도를 가진다. 그럼으로 결국 O(N x LlogL)의 시간복잡도를 가질 것이다.

**공간복잡도**

- 본 코드에서는 sorted_word 라는 별도의 변수를 만들어서 정렬된 값을 따로 보관하고 있다. 그럼으로 여기서는 단어의 길이 O(L)의 공간복잡도를 가진다. 이후 hashmap에서의 크기는 단어의 개수 N에 대하여 O(N)의 공간복잡도를 가진다.
전체적으로 O(L x N)의 공간복잡도를 가질 것이다.



---


### 📝 회고 / 추후 개선점
- 다른 풀이들을 찿아보니 DefaultDict를 사용하는 풀이가 다소 존재했다. 본인은 단순하게 not in 구문을 사용하여 hashmap을 구현했지만 defaultdict을 사용하면 문제 풀이과정은 1~2줄 정도는 더 단축될 수 있을것이라고 생각했다. 하지만 성능적으로는 유의미한 차이가 없을 것으로 생각된다.

---

