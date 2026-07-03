# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left=[]
        right=[]

        def preorder(node): #루트 기준 왼쪽 부분 탐색
            if node:
                left.append(node.val)
                preorder(node.left)
                preorder(node.right)
            else:
                left.append(None)
            

        def postorder(node): #루트 기준 오른쪽 부분 탐색
            if node:
                right.append(node.val)
                postorder(node.right)
                postorder(node.left)
            else:
                right.append(None)

        preorder(root.left)
        postorder(root.right)

        return right == left #양쪽 탐색 후 배열을 통한 비교
