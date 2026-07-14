---
# [LeetCode] 144. Binary Tree Preorder Traversal
---
### 📌 문제 링크
[LeetCode - 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/?envType=problem-list-v2&envId=depth-first-search)
---
### ⚠️ 제약조건
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
---
### 🛠️ 풀이 접근 및 핵심 로직
- 문제는 **Tree** 를 제공하며, 이 **Tree** 의 노드 데이터를 **Preorder** 순으로 출력하길 원한다. 현재노드 -> 현재노드의 왼쪽노드 -> 현재노드의 오른쪽 노드 순서로 조회가 되도록 우선순위를 설정하여 탐색을 진행하면 될 것이다. 
---
### 📊 복잡도 분석
**시간복잡도**

- 트리의 모든 노드는 결국 한번씩 지나가게 된다. 그렇기에 시간복잡도는 **O(N)**이라고 생각하면 될 것이다.

**공간복잡도**

- 트리가 최악의 경우 편향트리라고 가정하고 그 트리의 노드 개수가 **N** 개라고 가정했을때, 재귀를 통해 작동하는 현 코드 원리 상, 재귀호출스택을 사용하면 **O(N)** 의 공간복잡도를 가지게 된다.
---
### 📝 회고 / 추후 개선점
- **Preorder, Inorder, Postorder** 는 전공수업 시간에 배웠던 **tree traversal** 내용이라 쉽게 접근이 가능했었다. 
---
