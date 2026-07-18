---
# [LeetCode] 226. Invert Binary Tree
---

### 📌 문제 링크

[LeetCode - 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=depth-first-search)
---
### ⚠️ 제약조건

-   The number of nodes in the tree is in the range \[0, 100\].
-   \-100 <= Node.val <= 100
---
### 🛠️ 풀이 접근 및 핵심 로직

-   핵심 로직은 매우 단순하다. **DFS** 알고리즘을 사용해서 **traversal** 하면서 아래에서부터 전부 **invert** 해주면 끝나고 난 후에는 전체적으로 **invert** 되게 된다. 직관적으로 이해하기 위해서 그림을 그려보자.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio" src="https://github.com/user-attachments/assets/7bba712f-06ab-412a-9d97-f048e6e8e836" />


-   위와 같은 트리가 있다고 해보자. 재귀로 순회하게 되면 **1**의 노드 값을 가지는 값에 도착하게 될 것이다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (1)" src="https://github.com/user-attachments/assets/a43f9ae8-7834-4738-8c24-2e876252ce8a" />


-   이렇게 **1**에 도달하게 되어도 **left, right** 자식노드가 부재하니 아무것도 계산되지 않고 부모노드인 **3**으로 반환되며 자동으로 **2**로 가게 된다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (3)" src="https://github.com/user-attachments/assets/d4043010-068a-4db1-a121-58315527a7c1" />


-   **2**에 도달하고 나서도 결국 이전과 같은 이유로 부모 노드인 **3**으로 반환되게 된다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (4)" src="https://github.com/user-attachments/assets/3c2e3438-066e-41b2-ae85-9098f0f6949e" />


-   부모노드 **3**에 도달하고 나서 **right** 자식노드와 **left** 자식노드를 **swap** 하게 된다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (5)" src="https://github.com/user-attachments/assets/2e6b772d-cc9d-4390-a352-376d8e8d7a42" />


-   이후 **3**의 부모노드인 **5**로 올라간다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (6)" src="https://github.com/user-attachments/assets/d62e1b03-32f1-456f-9fc8-17d9dbda0948" />


-   여기서 **5** 기준에서 **left** 노드 부분은 조회가 끝났지만 **right**는 그러지 않다. 그러므로, **right** 노드 부분을 조회한다. 

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (7)" src="https://github.com/user-attachments/assets/904f470b-382a-4d1c-bf60-f7bd947dc611" />


-   전체 노드 기준 왼쪽 부분과 똑같은 논리로 **6**과 **7**이 처리되며, 이 처리과정은 넘어가도록 하겠다. 결국 이 과정을 통하여 **8** 을 가지는 노드의 자식노드 **left**와 **right**가 **swap** 된다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (8)" src="https://github.com/user-attachments/assets/1329056a-16f7-462b-92f3-3bb9dda2dec0" />


-   **8**의 처리과정이 끝났으니 다시 **5** 노드로 올라간다. 그렇게 되면 왼쪽 부분과 오른쪽 부분의 조회가 전부 끝났다고 할 수 있다. 여기서 두 부분의 **swap**이 이루어진다.

<img width="281" height="201" alt="제목 없는 다이어그램 drawio (9)" src="https://github.com/user-attachments/assets/55a2517f-46f2-41b6-83a9-3b16f932f9d9" />


-   이렇게 **root** 기준으로의 **swap** 이 끝나게 되면 전체 **tree**의 **invert** 가 성공적으로 적용되는 것을 직관적으로 이해해볼 수 있다.
---
### 📊 복잡도 분석

**시간복잡도**

-   트리의 노드는 한번씩 조회가 된다. **O(N)** 의 시간복잡도를 가진다.

**공간복잡도**

-   **left** 와 **right** 를 사용하여 조회하는 과정에서의 **swap**을 진행한다. 여기에서는 **O(1)** 의 공간복잡도를 가진다고 할 수 있다.
-   **재귀호출스택**에서 최악의 경우에 **O(N)**의 공간복잡도를 가진다.
---

### 📝 회고 / 추후 개선점

-   생각보다 문제 로직의 완전한 이해를 하기 위한 시간이 소모되었다. 뭔가 헷갈리는 포인트들이 생겨나서 그려보며 이해하는 과정이 있었다. **DFS** 알고리즘으로 하위에서부터 계속 **swap** 하면 되지 않을까 라는 생각은 처음부터 있었지만 이중으로 **swap**이 되서 원상복구가 되는 경우가 혹시나 있지 않을까 하는 걱정에 대한 증명이 필요했다. 하지만 생각을 해보면 단순하다. 한번 **swap** 을 진행한 부분은 동일한 레벨에 있어서 다시 **swap** 되지 않게 하면 그만이였다. 실제로도 가장 단순하게 코드를 구현해도 그렇게 작동한다.

---
