

---


# [LeetCode] 2. Add Two Numbers


---


### 📌 문제 링크
[LeetCode - 2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)


---

### ⚠️ 제약조건
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.



---


### 🛠️ 풀이 접근 및 핵심 로직
- 두개의 Linked List의 덧셈에 있어서 먼저 결과값을 반환할 Linked List를 만들기 위하여 새로운 head 변수를 선언하여 새로운 노드를 가르키게 했다. 그리고 실제로 노드간 이동하며 덧셈을 하기위하여 curr 변수를 선언하여 head 변수가 가르키는 노드를 새로 지정하여, carry를 반영하여 덧셈이 가능하게 구현하였다. while 반복문에서는 l1와 l2는 끝났지만 carry가 남아있어도 더해질 수 있다는 점을 감안하여 조건을 지정했다. 마지막에는 head를 반환하게되면 앞에 원하지 않는 값과 함께 반환이 될 수 있다는 점을 고려하여 head.next를 사용하여 올바른 결과값을 반환하도록 구현했다.
---


### 📊 복잡도 분석
**시간복잡도**
- 결과값을 구하기 위하여 l1를 순회하야한다. l1의 크기 N에 대하여 O(N)의 시간복잡도를 가지며, l2의 크기 N에 대하여도 O(N)의 시간복잡도를 가진다. carry가 남아있는 경우에 최대 1번 더 연산이 필요할 수 있으나 trivial 한 경우라고 판단하기에 결론적으로 O(N)의 시간복잡도를 가진다고 평가했다.


**공간복잡도**
- 결과를 반환하기 위한 Linked List를 만들어야한다. 그렇기에 l1과 l2중 가장 길이가 긴 Linked List의 크기 N에 대하여 기본적으로 O(N)의 공간복잡도를 가진다. 이외에도 val1 val2 carry x 와 같은 연산 및 저장을 위한 변수 사용을 위하여 O(1)의 공간복잡도를 가진다.
- 결과적으로 O(N)의 공간복잡도를 가진다.




---


### 📝 회고 / 추후 개선점
- 다른사람들이 푼 풀이 중에서 성능이 높게 나온 코드를 위주로 살펴본 결과 나의 코드는 self를 너무 많이 사용했다는 점이 생각보다 높은 성능 차이를 발생시켰으며 또한 이것이 호출된 횟수마다 필요없이 공간을 계속 누적해서 차지한다는 점이 비효율적이라는 사실을 파악했다. 이러한 점은 다른 문제를 풀면서도 분명히 의식하며 개선해야 할 것이다.

---

