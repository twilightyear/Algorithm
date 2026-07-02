# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1,n2):
            if n1 == None and n2 == None: #둘다 None일때
                return True
            elif n1 == None or n2 == None: #한쪽만 None일때
                return False
            elif n1.val != n2.val: #값이 다르다면
                return False

            left = dfs(n1.left, n2.left)
            right = dfs(n1.right, n2.left)

            return (left and right)
        return dfs(p,q)
