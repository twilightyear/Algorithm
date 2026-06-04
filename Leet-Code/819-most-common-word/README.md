

---


# [LeetCode] 819. Most Common Word


---


### 📌 문제 링크
[LeetCode - Most Common Word](https://leetcode.com/problems/most-common-word/description/)


---

### ⚠️ 제약조건
- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters.



---


### 🛠️ 풀이 접근 및 핵심 로직

본 문제에서는 주어진 데이터에서 가장 흔하게 등장하는 단어를 구하는 대신 상당한 제약을 걸었다.
먼저 금지된 단어가 있으며 이외에도 대소문자 구분을 하지 않으며 구두점 또한 무시하라고 되어있다.

풀어서 할 수 있겠지만 파이썬의 장점 중 하나인 리스트 컴프리헨션을 활용하여 성능과 간결함을 챙길 수 있겠다.

이후에는 Hashmap 의 원리를 가진 Counter를 사용하여 빠르게 가장 빈번한 출현을 한 데이터를 추출해낼 수 있겠다.
---


### 📊 복잡도 분석
**시간복잡도**

- 리스트 컴프리헨션 과정에서는 paragraph에 정규표현식을 사용하여 필요없는 구두점을 삭제한다. 이 과정에서 O(N)의 시간복잡도가 발생한다. 여기서 .lower()은 상관없겠지만 not in banned 라는 조건에서는 banned 리스트에 2개 이상의 값이 들어간다면 여기서 banned 리스트의 길이 B로 전체적으로 O(N x B)의 시간복잡도가 발생한다고 볼 수 있다. 하지만 본 문제에서는 banned.length는 많아봤자 100개이다. B는 상수항으로 취급해도 괜찮다고 판단했다.

- Counter의 자체 추출 시간복잡도는 서로 다른 단어의 개수 K 에 대하여 O(K)이다. 이외에도 생성과정에서 O(N)의 시간복잡도를 가진다. 하지만 결국 해봤자 K<=N임으로 결국 전체적으로 O(N)의 시간복잡도를 가진다.


**공간복잡도**

- 리스트 컴프리헨션 과정에서 words 라는 리스트와 word라는 임시 변수를 사용한다. word는 O(1)의 공간복잡도를 가지지만 words는 O(N)의 공간복잡도를 가진다.

- Counter를 사용하며 결국 O(K)의 공간복잡도를 가질 수 밖에 없다.

- 그러므로 결과적으로 O(N)의 공간복잡도를 가진다고 할 수 있다. (K<=N)





---


### 📝 회고 / 추후 개선점
시간복잡도의 관점에서 나름 우수한 풀이였다고 생각했으나, 똑같은 문제지만 훨씬 빠른 코드를 하나 보았다.

다른 풀이들은 내부적으로 C언어로 돌아가는 maketrans 과 translate등을 사용했기에 다른 코드보다 빠른 모습을 보였다.

이외에도 most_common까지 한줄에 넣어서 풀이를 간략화한 사람도 있었다.

정말 사소한 디테일이 어떻게 성능에 영향을 주는지 알아볼 수 있었다.

---

