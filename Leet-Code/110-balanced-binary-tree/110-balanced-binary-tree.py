### [ LeetCode ] 110. Balanced Binary Tree

### 📌 문제 링크

[LeetCode - Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

### ⚠️ 제약조건

- The number of nodes in the tree is in the range [0, 5000].
- -104 <= Node.val <= 104

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 아래에서부터 검사를 한다. 높이가 0 인 지점인 아래에서부터 검사하며, 왼쪽노드와 오른쪽 노드의 차이가 2 이상인 경우라면 -1 를 반환해버리며, 이는 위로 올라가는 과정에서 계속 비교할 필요도 없이 -1 이 올라가도록 한다. 이러한 불균형이 없다면 마지막 부분에서 왼쪽 자식 노드까지의 높이와 오른쪽 노드까지의 높이 중에서 더 큰 높이에 1을 더한 현재 높이값을 계속 최신화하는 방식으로 올려보낸다. 

### 📝 추후 개선점

- 사실 접근 1번 자체가 하향식으로 문제를 풀려고 하다가 실패해서 전환을 진행한 코드이다. 위에서부터 BFS 를 이용해서 내려보내는 방식을 사용해야하나 싶었지만, 굳이그럴 필요 없이 아래에서부터 상향식 방식으로 노드의 개수 N 개에 대하여 O(N) 의 시간복잡도와 공간복잡도를 가지게 할 수 있었다.

### 💻 풀이 코드

```python
# 풀이 1 (Tree)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0

            left_height = get_height(node.left)
            if left_height == -1:
                return -1

            right_height = get_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1
        
        return get_height(root) != -1
```

### 🤔 고찰

- 군대를 전역하자마자 해커톤에 참여하고, 상위팀에 선정되어 전시회 준비 및 상주발표에 몰두하여 문제를 푸는 것에 요즘 조금 소홀해진 것 같다. 이러한 알고리즘적 사고방식은 오래 해볼 수록 실력과 사고방식 확립에 도움이 된다고 생각하기에, 꾸준함을 잃지 말아야한다고 생각했다.
