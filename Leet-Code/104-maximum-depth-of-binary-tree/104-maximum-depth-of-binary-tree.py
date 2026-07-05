# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node: #노드가 존재하지 않으면 기존 depth 반환
                return depth
            left = dfs(node.left, depth+1) #왼쪽 노드에 depth+1 을 통하여 재귀 호출
            right = dfs(node.right, depth+1) #오른쪽 노드에 depth+1 을 통하여 재귀 호출
            return max(left, right) #양쪽 노드중에서 더 깊은 depth 를 가진 값만 반환
        
        return dfs(root, 0) #루트를 기준으로 depth의 초기값은 0으로 설정하여 재귀 시작
