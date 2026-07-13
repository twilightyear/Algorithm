# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validation(node, low=float('-inf'), high=float('inf')):

            if not node: #빈 노드도 유효하도록 설정
                return True

            if (node.val >= high or node.val <= low): #범위를 벗어난다면 False 반환
                return False

            #재귀를 통하여 왼쪽 자식 노드는 low 부터 현재노드의 값의 범위를 가지도록 설정한다.
            #같은 논리로 오른쪽 자식 노드는 현재노드의 값 부터 high 값의 범위를 가지도록 설정한다.
            return validation(node.left, low, node.val) and validation(node.right, node.val, high)

        return validation(root)     
