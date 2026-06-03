

---


# [LeetCode] 937. Reorder Data in Log Files


---


### 📌 문제 링크
[LeetCode - Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/)


---

### ⚠️ 제약조건
- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- All the tokens of logs[i] are separated by a single space.
- logs[i] is guaranteed to have an identifier and at least one word after the identifier.



---


### 🛠️ 풀이 접근 및 핵심 로직
- 하나의 로그는 [ 식별자, 타입, 타입,  ... ] 의 형식으로 이루어진다. 여기서 타입은 숫자가 될 수도 있고 문자열이 될 수 있다. 먼저 이 타입을 기준으로 문자열로 이루어진 로그들이 숫자로 된 로그들 보다 먼저 정렬되어야 한다. 문자열간에서는 사전순으로 정렬하고 숫자는 그대로 둔다. 우선순위가 동일하다면 즉 내용이 똑같다면 그 것들의 식별자를 기준으로 사전순으로 정렬한다.

- Python의 sorted()는 숫자가 문자보다 우선되어 정렬된다. 그럼으로 [식별자, 타입, 타입, ... ]의 요소에서 인덱스 0의 요소인 식별자 기준으로 숫자와 문자열을 다로 배열로 보관하고 이후 인덱스 1 이후의 요소들을 슬라이싱하고 식별자를 슬라이싱 하여 활용한다면 쉽게 해결이 가능할 것이다.
---


### 📊 복잡도 분석
**시간복잡도**

log의 길이 L, logs의 크기 N 일때, 루프의 내부에서 문자열 조작과 관련된 함수들은 O(L)의 시간복잡도를 가지나, 본 문제에서는 길어도 100글자 이내라고 사전 조건을 정해줬기에 상수로 취급해도 무방하다고 판단했다. 그렇기에 O(1)이다.

이후 정렬 과정은 Python의 내장 함수인 sort를 사용했다. Timsort 원리를 사용하는 본 함수는 O(nlogn)의 시간복잡도를 가지나, lambda의 사용으로 O(L x nlogn)이라고 생각해야한다. 그러나 위에서 설명했던 것과 같은 원리로 상수취급을 하게 되면 O(nlogn)으로 볼 수 있다.

그러므로, 총 전체적인 시간복잡도는 O(nlogn)이라고 볼 수 있다.


**공간복잡도**
먼저 logs의 길이 N에서 두번 나누어져서 string 배열과 number 배열에 log가 들어간다. 이후에는 append를 활용하여 결국 logs의 길이 N 만큼 결국 전부 분배되게 된다. 그러니 이것은 O(N)의 공간복잡도를 가질 것이다. 이후에는 for 문이 돌아가며 log를 할당하는데, log라는 객체를 재사용할 것이기에 여기서의 공간복잡도는 O(1)를 가질것이다.

내장함수 sort()는 sorted()와 다르게 원본 배열을 수정하는 함수로, 따로 공간을 사용하지 않는다.

그러므로, 총 전체적인 공간복잡도는 O(N)이라고 볼 수 있다.




---


### 📝 회고 / 추후 개선점
본 문제를 풀며, 

Wrong Answer
65 / 66 testcases passed

Analysis

Editorial
Input
logs =
["dig1 8 1 5 1"," let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

Use Testcase
Output
["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Expected
["let3 art zero"," let1 art can","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

이라는 결과가 마지막에 나와서 무척 당황했다.

왜 틀렸는지 보다가 " let1 art can"의 공백이 있다는 것을 확인했다. 본 문제의 조건과 맞지 않는다.


> **All the tokens of logs[i] are separated by a single space.**

아마 공백과 관련된 처리 관련해서 함정을 숨겨놓으려는 의도였던 것 같지만 문제의 조건에서 벗어나버린 문제가 되어버린 것 같다.


---

