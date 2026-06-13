# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.head = ListNode() #결과값을 반환할 head 지정
        self.curr = self.head #데이터의 순차적인 보관을 위하여 새로운 변수 할당
        carry=0 #자릿수 올림을 위한 변수 초기화

        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = (val1+val2+carry) #합계 먼저 계산.

            carry = total//10
            x = total%10

            self.curr.next = ListNode(x) #다음 노드에 값 할당

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            self.curr = self.curr.next #다음 노드로 이동

        return self.head.next #head가 가르키는 노드부터 시작되는 Linked List 반환
