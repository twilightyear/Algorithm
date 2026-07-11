

---


# [LeetCode] 112. Path Sum


---


### 📌 문제 링크
[LeetCode - Template](https://leetcode.com/problems/path-sum/description/?envType=problem-list-v2&envId=depth-first-search)


---

### ⚠️ 제약조건

- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000


---


### 🛠️ 풀이 접근 및 핵심 로직
- 본 문제는 Tree에서 아래로 내려가면서 값을 더하고, 그 값이 leaf 노드에 도달했을때 targetSum을 만족하는 경우가 있는지 검사하는 문제이다. 본 문제는 targetSum을 가지고 재귀하며 노드의 값을 빼나가고, leaf 노드에서 0이 되는지 검사하면 될 것이다.
---


### 📊 복잡도 분석
**시간복잡도**
- Tree의 모든 노드를 재귀를 사용하여 예외없이 전부 검사한다. Tree의 길이 N에 대하여 O(N)의 시간복잡도를 가질 것이다.

**공간복잡도**
- Tree의 노드를 재귀적으로 탐색하는 과정에서 재귀 호출 스택을 사용한다. 최악의 경우 Binary Tree는 편향 트리의 형태로 나타날 수 있다. 이러한 경우에서 Tree의 길이 N에 대하여 O(N)의 공간복잡도를 가질 수 있다. left와 right 등의 추가적인 변수 공간 할당이 존재한다. O(1)의 공간복잡도를 가진다. 결과적으로 O(N)의 공간복잡도를 가진다고 할 수 있다.




---


### 📝 회고 / 추후 개선점
- 처음 문제를 보자마자 풀었을때 논리적으로 맞다고 생각하고 제출을 눌렀지만 일부의 경우에서 오류가 발생한것을 볼 수 있었다. 그 이유는 바로 조회 과정에 있었다. 단순하게 targetSum-val=0만 만족하는게 하나만 있으면 true라고 생각하여 코드를 제출했지만 오류가 발생했다. 그 이유는 targetSum-val=0이라고 하더라도 leaf 노드가 아니라면 올바르지 않기 때문이다. 실제로도 실패한 경우의 케이스를 살펴보니 노드가 총 2개인 트리, root값은 1이고 left 노드 값은 2인 트리의 경우에서 targetSum이 1인 경우에서 root값이 leaf가 아님에도 불구하고 1-1=0 이라는 계산만 사용하여 올바르지 않은 답을 반환한 경우가 존재했다. 이를 개선하기 위하여 leaf 노드 확인 조건을 만들어서 leaf 노드의 경우에만 확인을 진행하도록 하고 left or right를 통하여 leaf 노드들중 하나라도 True인 경우에 재귀를 통하여 결론적으로 True가 반환될 수 있도록 구현할 수 있었다.

