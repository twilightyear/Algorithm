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
