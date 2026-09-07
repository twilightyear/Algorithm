# 풀이 1 (Floyd's Cycle Algorihm)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        fast = head
        slow = head

        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next

            if(fast == slow):
                return True

        return False
