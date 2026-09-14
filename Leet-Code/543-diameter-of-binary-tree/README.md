### [ LeetCode ] 543. Diameter of Binary Tree

### 📌 문제 링크

[LeetCode - Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)

### ⚠️ 제약조건

- The number of nodes in the tree is in the range [1, 104].
- -100 <= Node.val <= 100

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - DFS 를 이용하여 왼쪽 자식부터 전부 살핀다. 여기서 왼쪽 자식의 끝에 도달했을때와 같은 노드가 없는 지점이라면 0을 반환하며 재귀적으로 구성한다. 이렇게 왼쪽 자식과 오른쪽 자식에 있어서 탐색을 할때 더 1 + max(left, right) 를 통하여 오른쪽 왼쪽 중에서 더 긴 depth 를 가진 길이를 반환한다. 여기서 우리의 목표는 diameter 의 최댓값을 구하는 만큼, 단순 left 와 right 의 최댓값을 구하여 최대 길이만을 반환하는 것이 아닌, left + right, 즉 diameter 값을 max() 를 사용하여 최신화를 계속 해주는 방식으로 구현할 수 있다.
  - 최악의 경우에서도 노드의 개수 N 개에 대하여 이진 트리는 편향 트리가 될 수 있는데, 이러한 경우에서도 N 번만 탐색하면 되니 O(N) 의 시간복잡도를 가지지만, 재귀호출 스택때문에 O(N) 의 공간복잡도를 가진다고 할 수 있다.

### 📝 추후 개선점

-  코드에서 self.max_diameter = 0 로 사용하는 것을 nonlocal max_diameter = 0 를 DFS 함수 내부에 사용한다면 속성 조회를 최적화할 수 있다. 이외에도 dfs 구현에 있어서 아직까지 직관적으로 바로 풀이가 나오는 실력이 되지 않는것 같다. 꾸준한 연습하자.

### 💻 풀이 코드

```python
# 풀이 1 (DFS)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            #Max 값 갱신
            self.max_diameter = max(self.max_diameter, left + right)
            
            #더 깊은 depth 를 가지는 자식의 길이 반환
            return 1 + max(left, right)

        dfs(root)

        return self.max_diameter
```
