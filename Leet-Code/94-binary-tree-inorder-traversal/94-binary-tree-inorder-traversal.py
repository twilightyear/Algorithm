# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = [] #결과 반환을 위한 배열 선언

        def inorder(node): #Inorder 순으로 조회하기 위한 재귀 함수
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root) #root를 시작으로 함수 호출

        return result
