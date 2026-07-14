# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = [] #결과 출력용 리스트

        def DFS(root): #재귀를 위한 함수
            if not root:
                return

            result.append(root.val) #Preorder 순으로 구성
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)

        return result
