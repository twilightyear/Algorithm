#풀이 1 (Linked List)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        #중간 구하기 (Floyds)
        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #뒷부분 화살표 역전
        prev = None
        curr = slow.next
        slow.next = None

        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #앞부분과 뒷부분 교차
        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2
