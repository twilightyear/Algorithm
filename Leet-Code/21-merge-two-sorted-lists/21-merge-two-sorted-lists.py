# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode() #결과를 반환할 더미 Linked List 선언
        curr = head

        while(list1 and list2): #둘다 값이 남아있을때만 루프

            if(list1.val<list2.val):
                curr.next = list1 #굳이 노드를 새로 만들 필요 없이 노드 재사용
                list1 = list1.next
            else:
                curr.next = list2 #굳이 노드를 새로 만들 필요 없이 노드 재사용
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2 #남은 Linked List는 결과 뒤에 그대로 연결

        return head.next
