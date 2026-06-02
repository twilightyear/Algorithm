

---


# [LeetCode] 344. Reverse String


---


### 📌 문제 링크
[LeetCode - Reverse String](https://leetcode.com/problems/reverse-string/description/)


---

### ⚠️ 제약조건
- 1 <= s.length <= 105
- s[i] is a printable ascii character.



---


### 🛠️ 풀이 접근 및 핵심 로직
배열이 입력으로 들어온다. 투포인터로 문제를 해결 할 수 있었다. 배열의 양끝을 left right로 잡은 후 left<=right라는 조건으로 돌려준다.

---


### 📊 복잡도 분석
**시간복잡도**
배열의 크기에 비례하여 탐색을 하여 tmp를 사용한 자리 바꿈이 이루어진다. 그렇기에 O(N)의 시간복잡도를 가진다.

**공간복잡도**
left right와 tmp의 추가적인 공간사용이 있다. 그렇기에 O(1)의 공간복잡도를 가진다.




---


### 📝 회고 / 추후 개선점
Python의 내장 함수인 .reverse()를 사용한다면 아주 간단하게 작성할 수도 있으며 투포인터보다 빠른 구동이 가능하다는 점을 파악했다.

---

