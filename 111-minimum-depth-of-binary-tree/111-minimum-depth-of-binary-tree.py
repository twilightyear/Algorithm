# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #해당 노드가 없다면 0 반환.
            return 0
        else: 
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            
            if(left!=0 and right!=0): #자식 전부 존재
                return min(left,right)+1 #가장 적은 수 택하고 1 증가하여 반환
            else : #자식이 1개라도 없다면
                return left+right+1 #따로 조건문 사용하지 않고 만약 자식이 존재한다면 그 노드 반환
