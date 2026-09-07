### [ LeetCode ] 141. Linked List Cycle

### 📌 문제 링크

[LeetCode - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

### ⚠️ 제약조건

- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

### 🛠️ 풀이 접근 및 분석

> Given head, the head of a linked list, determine if the linked list has a cycle in it.

> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

> Return true if there is a cycle in the linked list. Otherwise, return false.

-   **접근 1**
  - 연결 리스트의 순환 여부를 확인하기 위하여 Floyd's Cycle Algorithm 을 사용하면 쉽게 파악할 수 있다. 하나의 조회 커서는 1칸씩 이동하며, 다른 하나의 조회 커서는 2칸씩 이동하게끔 한다면, 만약 이 두 커서가 만나게 되는 연결 리스트는 순환 연결 리스트라는 점을 사용한다. 여기서 추가적인 커서를 사용했기에 O(1) 의 공간복잡도를 가지나, 하나하나 조회가 필요하기 때문에, 최악의 경우 O(N) 의 시간복잡도를 가진다.

  - 문제를 풀고나서, 다른 사람들의 더욱 높은 성능을 지닌 코드가 있다는 것을 파악하고 해당 코드들을 살펴보았다. 여기서 

### 📝 추후 개선점

  - 문제를 풀고나서, 다른 사람들의 더욱 높은 성능을 지닌 코드가 있다는 것을 파악하고 해당 코드들을 살펴보았다. Floyd's Cycle Algorihm 을 사용한다는 점은 똑같았으나, 불필요한 조건문들을 삭제할 여지를 확인했다. 내 코드가 사용하는 기준점을 한칸 당긴 기준점에서 검사를 한다면 최초에 head 를 검사할 필요도 없어지면서도, while 문 조건 검사에서 현재 값의 next와 next.next 까지 확인할 필요 없이, 기준을 당겼기에, 현재 값이 가르키는곳과 next값만 확인한다면 조회 횟수를 상당히 단축시킬 수 있었다. 아래 코드처럼 개선이 가능했다.

```python
# Optimized

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

            if(fast == slow):
                return True

        return False
```

### 💻 풀이 코드

```python
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
```

### 🤔 고찰

- 알고리즘을 공부하면서 얼핏 들었던 Floyd's Cycle Algorithm 이 딱 생각나서 적절하게 풀어볼 수 있었던 문제였다. 이렇게 문제를 보자마자 어떤 자료구조를 사용해서 어떻게 구현하면 될지 빠르게 파악하는 역량은 기본이라고 생각하는 만큼 앞으로도 꾸준히 공부할 필요가 있다.
