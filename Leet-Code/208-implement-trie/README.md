

---


# [LeetCode] 208. Implement Trie (Prefix Tree)


---


### 📌 문제 링크
[LeetCode - Reverse Integer](https://leetcode.com/problems/implement-trie-prefix-tree/description/)


---

### ⚠️ 제약조건
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 104 calls in total will be made to insert, search, and startsWith.
---


### 🛠️ 풀이 접근 및 핵심 로직
- Trie는 TrieNode를 Tree와 Hashmap을 활용하여 구현할 수 있는 일종의 자료구조이다. Node를 self.child, self.is_end와 함께 정의하여 노드가 leaf 노드인지와 dictionary 를 활용한 hashmap을 통하여 자식 노드들이 무엇이 있는지 관리 할 수 있다.


---


### 📊 복잡도 분석
**시간복잡도**

- Trie class에서 insert에서는 for char in word 를 사용하는데, 이것의 시간복잡도는 O(L)이며 L은 단어의 길이다. 이렇게 for문 안에 if char not in .child 의 형태, 즉 hashmap의 요소가 있는지 없는지 확인하기 위하여 in 을 쓰는데, 이것은 hashmap의 원리, 즉 문자열을 일종의 함수에 통과시키고 그것을 바로 주소로 활용하는 특성에 있어서 시간복잡도는 O(1)이다. if문이 끝나고 나서는 다음 자식노드로 이동하기 위하여 current_node = current_node.child[char]을 사용한다. 이것 또한 위에서 서술한 hashmap의 원리를 통하여 접근되는데 마찬가지로 O(1)의 시간복잡도를 가진다.

- insert를 제외한 search, startsWith 전부 동일한 로직으로 동작한다. 이에 따라서 insert, search, startsWith 모두 O(L)의 시간복잡도를 가진다.


**공간복잡도**

- 본 Trie는 노드당 1개의 char를 저장한다. 만약 n개의 단어가 있고 단어의 평균 길이가 L이라고 하면 공간복잡도는 O(NxL)로 표현하는 것이 맞을 것이다.


---


### 📝 회고 / 추후 개선점

- 함수들 로직 내에서 current_node.child[char] = Node() 와 같은 기능을 사용하기 위하여 항상 if문을 통한 확인을 동반하고 있다. 하지만 애초에 일반 dict이 아니라 collections 라이브러리에서 사용 가능한 defaultdict을 사용한다면 if문을 사용하지 않고 간결하게 코드 작성이 가능할 것이고 미약하게나마 성능의 개선이 있을 수 있을 것이다.

- 여기서 사용한 class로 구현 한 것 자체가 공간복잡도 측면에서 상대적으로 무겁다고 할 수 있다. 그럼으로 Node 부분에 __slots__ 을 사용하여 사용하고자 하는 속성을 명시해주어 낭비되는 공간을 줄일 수 있다. 여기서는 __slots__ = ["child","is_end"]를 쓸 수 있었을 것이다. 마찬가지로 동일한 이유로 Trie에도 정의해두면 공간적으로 상대적인 효율성이 있을것이다.
---

