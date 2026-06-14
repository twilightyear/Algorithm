

---


# [LeetCode] 21. Merge Two Sorted Lists


---


### 📌 문제 링크
[LeetCode - 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)


---

### ⚠️ 제약조건
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.



---


### 🛠️ 풀이 접근 및 핵심 로직
- 두 Linked List는 정렬되어서 주어진다. 그렇기에 앞 노드부터 순차적으로 비교해가면서 next를 통하여 이동해주면 된다. 저번에 Linked List를 풀며 결과 반환용 Linked List를 만들때 계속 노드를 새로 만들었던 적이 있다. 공간적으로 매우 비효율적이기에 이번에는 같은 실수를 반복하지 않도록 앞의 값을 비교하고 결과 Linked List에 할당할때 작은 Node를 그대로 할당하여 재사용을 해주었다. 
- while문은 둘중 하나만 끝나도 종료되도록 설정하였다. 왜냐하면 정렬되어있다는 특성 덕에 하나가 끝났다고 가정하면 다른 하나가 만약 더 남아있다는 경우에서는 이 Linked List의 남은 부분은 무조건 앞 부분보다 큰 값들을 가지게 된다. 그렇기에 결과를 반환하고자 하는 Linked List에 그대로 이어서 붙이면 군더더기 없이 잘 작동할 것이다.
---


### 📊 복잡도 분석
**시간복잡도**
본 코드에서는 List1의 길이 N과 List2의 길이 M에 대하여 더 작은 길이 Min(N,M)에 대하여 순회를 거치기 떄문에 O(min(N,M))의 시간복잡도를 가지게 된다. 더 긴 길이에 대해서는 굳이 전체 순회를 거치지 않기 때문이다.

**공간복잡도**
결과를 반환하기위하여 head, curr부분을 선언하면서 O(1)의 공간복잡도를 가지게 되었지만, 이후 할당하는 과정에서는 입력으로 들어온 Linked List를 재사용함으로써 공간복잡도의 측면에서의 효율성을 극대화하였다. 마지막 반환하기 전에 남은 부분이 있다면 붙이는 부분에서도 결국 똑같은 원리로 재사용을 하는 것이기 때문에 전체적으로 O(1)의 공간복잡도를 가지게 된다.




---


### 📝 회고 / 추후 개선점
이전에 Linked List 문제를 풀어보고 아쉬웠던 점들을 적극 반영하여 코드를 구성해보았다. 노드의 재사용 측면이 매우 효율적인 결과를 가져왔으며, 실제로도 본 문제 전체 사용자 제출 기록 내에서 상위권의 속도를 보여주었다.

---

