

---


# [LeetCode] 94. Binary Tree Inorder Traversal


---


### 📌 문제 링크
[LeetCode - Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=depth-first-search)


---

### ⚠️ 제약조건
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100



---


### 🛠️ 풀이 접근 및 핵심 로직
- 문제에서 원하는 조회 방식은 inorder 방식으로, 함수내에 DFS 함수를 정의하고 inorder 방식으로 조회를 할 수 있게 재귀적인 논리로 구현해주며 최초에 정의했던 결과 반환용 배열에 순차적으로 추가해주면 적절하게 문제가 해결될 것이라고 판단했다.

---


### 📊 복잡도 분석
**시간복잡도**
- 최악의 경우인 노드 개수가 N개인 편향 트리인 경우에도 결국 N번의 재귀 스택을 통한 조회가 필요하다. O(N)의 시간복잡도를 가진다.

**공간복잡도**
- 결과 반환용 배열은 최악의 경우 null 이 없다고 하면 결국 노드의 개수 N개만큼의 데이터가 들어가서 반환되게 되는데, O(N)의 공간복잡도를 가진다. 이외에도 재귀 호출 스택에 있어서 노드 개수가 N개인 편향트리라는 최악의 경우를 상정해도 O(N)의 공간복잡도를 가진다. 결과적으로 O(N)의 공간복잡도를 가진다고 할 수 있다.




---


### 📝 회고 / 추후 개선점
- DFS 문제들을 집중적으로 풀어보며, 학부 전공시간에 공부했었던 preorder, inorder, postorder 순서의 조회를 다시 활용해보며 실질적으로 적용해볼 수 있는 기회가 되었다. 이 문제는 어떻게 풀지 답을 거의 알려주고 풀어보는 방식에 가까웠으나, 난이도가 있는 문제들을 이제 풀어보며 DFS 유형에서의 문제해결능력을 기르고 싶다. 이외에도 계속 재귀로 문제를 풀어보고 있지만, 다른 사람들이 풀어본 풀이 중에서 iteration 을 이용한 풀이도 간혹 볼 수 있었다. 이러한 풀이법도 적용하여 공부해보겠다.

---

