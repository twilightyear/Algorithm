

---


# [LeetCode] 14. Longest Common Prefix

---


### 📌 문제 링크
[LeetCode - 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)


---

### ⚠️ 제약조건

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.


---


### 🛠️ 풀이 접근 및 핵심 로직
- 가장 긴 공통 접두사를 알기 위해서 먼저 입력 리스트를 정렬하면 쉽게 접근이 가능하다. 정렬된 리스트에서 가장 앞의 단어와 뒤의 단어만 보고 비교해보면 가장 긴 공통 접두어를 파악할 수 있다. 각 단어의 가장 앞의 알파벳부터 하나하나 비교하며 같은 부분까지를 공통 접두어로 출력하면 될 것이다.
---


### 📊 복잡도 분석
**시간복잡도**

- Python의 내장 sort는 Tim Sort를 사용한다. 이는 O(nlogn)의 시간복잡도를 가진다. first와 last 값을 저장하는데 인덱스로 값을 추출하기에 O(1)의 시간복잡도를 가진다. 그리고 두 단어에 대하여 전부 탐색을 하는데 최악의 경우에 첫번째 단어의 길이 N과 마지막 단어의 길이 M에 대하여 더 긴 길이 M에 대하여 O(M)의 시간복잡도를 가진다.

**공간복잡도**

- 추가적인 공간은 first와 last의 공간, 그리고 ptr만 할당한다. 그렇기에 O(1)의 공간복잡도를 가진다.



---


### 📝 회고 / 추후 개선점
가장 긴 공통 접두사를 파악하기 위하여 단어를 정렬하고 가장 첫 단어와 마지막 단어를 비교한다는 아이디어가 핵심이였던 문제였다.

---

