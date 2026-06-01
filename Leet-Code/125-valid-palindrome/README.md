

---


# [LeetCode] 125. Valid Palindrome


---


### 📌 문제 링크
[LeetCode - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=vwsipkvg)


---

### ⚠️ 제약조건
- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.



---


### 🛠️ 풀이 접근 및 핵심 로직

- 정규표현식을 지원하는 내장 라이브러리 re를 활용하여 문제에서 원하지 않는 형식을 쉽게 처리할 수 있다. 소문자화는 lower() 를 통하여 처리한다. 이후에는 문자열 인덱싱을 활용하여 원본과 비교하여 대칭 여부를 확인한다.
---


### 📊 복잡도 분석
**시간복잡도**
- lower()은 O(L) 와 re.sub의 해당 정규식은 O(L)로 동작한다. 서로 포함되는 구조가 아니니 O(L)으로 봐야 맞을것이다. 이후 슬라이싱도 동일하게 O(L)의 시간복잡도를 가진다. 종합적으로 최고차항인 O(L)이 최종 시간복잡도라고 할 수 있을것이다.


**공간복잡도**
- data에 정규표현식을 거친 문자열이 들어간다. 공간복잡도는 O(L)이 필요하다. 이후 data[::-1]의 슬라이싱을 사용하며 별도의 공간 O(L)이 필요하다. 그럼으로 최종적인 공간복잡도는 O(L)이라고 할 수 있을 것이다.




---


### 📝 회고 / 추후 개선점
충분히 빠르게 동작하는 시간복잡도 O(L) 공간복잡도 O(L)를 가지나, 만약 문자가 길어지게 된다면 리스트 컴프리헨션을 통하여 성능을 개선할 수 있을 것이다.

---

