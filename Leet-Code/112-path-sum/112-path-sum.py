# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root: #노드가 존재하지 않는다면
            return False

        if (not root.left) and (not root.right): #자식 노드가 아무것도 없다면(leaf 노드) 확인 진행
            if targetSum-root.val == 0: #targetSum에서 leaf 노드의 값을 빼서 0인지 검사
                return True #0이 나온다면, 즉 더해서 값이 나오는 path가 존재한다라는 값을 반환하기 위하여 True 반환.
            else:
                return False #아니라면 False 반환.
        
        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)

        return left or right #leaf 노드 검사시에 1개의 노드라도 만족한다면 결과는 True가 나와야한다. or을 사용해서 재귀를 마무리한다.
