### [ Programmers ] 올바른 괄호

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 괄호가 Valid 한지 확인하는 문제는 Stack 으로 해결 가능하다. 단일 괄호 종류에 대한 확인이니, ( 는 스택에 추가하며, ) 가 등장할 경우에는 스택에 ( 가 있는지 확인하여 삭제한다. 없다면 바로 False 를 반환하며, 마지막에 스택이 비어있는지 최종확인한다. 이렇게 한다면 s 의 길이 N 에 대하여 O(N) 의 시간복잡도와 O(N) 의 공간복잡도를 가진다.

### 📝 추후 개선점
  - 정말 신기한 접근법을 보았다. stack 을 사용하는 것이 아닌, 괄호의 종류가 이렇게 단일인 경우에서는 counter 를 사용하여 ( 가 등장하면 +1, ) 가 등장하면 -1 를 사용하여 연산하는 방식을 보았다. 하지만 ))(( 와 같은 경우는 제외해야하니 0 에서 -1 를 하려는 상황에서는 False 를 반환하게 하는 방어코드를 사용한다. 이렇게 한다면 공간복잡도를 O(1) 로 개선할 수 있다. 괄호 문제는 여럿 접해봤었으며, Stack 풀이법에만 매몰되어 있었는데, 이러한 접근 방식은 상당히 신선했다.

### 💻 풀이 코드

```python
# 풀이 1 (Stack)
from collections import deque

def solution(s):
    stack = deque()
    for char in s:
        if char == "(":
            stack.append(char)
            
        elif char == ")":
            if not stack or stack.pop() != "(":
                return False

    return len(stack) == 0
```
