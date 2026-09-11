### [ LeetCode ] 143. Reorder List

### 📌 문제 링크

[LeetCode - Reorder List](https://leetcode.com/problems/reorder-list/description/)

### ⚠️ 제약조건

- The number of nodes in the list is in the range [1, 5 * 104].
- 1 <= Node.val <= 1000

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 먼저 이전 Floyd's Cycle Algorithm 처럼 slow 와 fast 를 만들어서 fast 가 두배 속도로 움직인다고 하면 마지막에 도착했을때는 slow 는 중간일 것이다. 이를 기준으로 Linked List 를 분할할 필요가 있다.
  1. 중간지점에서 다음지점 끊어버리기
  2. prev 라는 끝값을 미리 만들어서 None 역할
  3. 다음지점부터 값이 원래 가르키던 것을 미리 따로 저장해두고 prev 가르키기
  4. 따로 미리 저장할 값을 이용하여 이동한 후 그 다점 값이 미리 가르키던것을 따로 저장해두고 prev 가르키기.
  5. 계속 반복 
  - 이렇게 된다면 중간을 기점으로의 뒷부분은 화살표가 역전되어 있을 것이다. 여기서 양 끝에서 화살표대로 진행하며, 올바르게 교차를 하게 된다면 문제를 풀 수 있다. 중간지점을 구하는 과정에서의 공간복잡도는 O(1), 시간복잡도는 O(n) 이며, 역전에서는 동일하게 공간복잡도는 O(1), 시간복잡도는 O(n), 교차하는 단계에서도 공간복잡도는 O(1), 시간복잡도는 O(n) 가 발생하여 결론적으로 총 공간복잡도는 O(1), 시간복잡도는 O(n) 이라고 할 수 있다.


### 📝 추후 개선점

- 사실 문제를 푸는데 너무 오래 걸렸다. 원래라면 30분 고민하고 못풀겠으면 다른 풀이를 살펴보며 체화하는 과정이 필요했지만, 욕심때문에 한시간 가량 붙잡고 있었던 것 같다. 지금 보면 그렇게 어려운 문제는 아니였던것 같지만 결국 경험 부족이라고밖에 생각이 들지 않는다. 그리고 이번 문제 이후로 고찰 부분은 빼버렸다. 추후 개선점 부분에 이제 같이 추가하려고 한다. 아무튼.. 꾸준히 열심히 풀어서 경험과 실력을 늘려서 이러한 문제는 간단하게 풀 수 있어야 할 것이다.

### 💻 풀이 코드

```python
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
```
