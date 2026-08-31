### [ LeetCode ] 150. Evaluate Reverse Polish Notation

### 📌 문제 링크

[LeetCode - Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

### ⚠️ 제약조건

- 1 <= tokens.length <= 104
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

### 🛠️ 풀이 접근 및 분석

> You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

> Evaluate the expression. Return an integer that represents the value of the expression.

> Note that:

> The valid operators are '+', '-', '*', and '/'.
> Each operand may be an integer or another expression.
> The division between two integers always truncates toward zero.
> There will not be any division by zero.
> The input represents a valid arithmetic expression in a reverse polish notation.
> The answer and all the intermediate calculations can be represented in a 32-bit integer.

-   **접근 1**
  - 이번 문제는 Postfix Notation 에 대하여 연산을 진행하면 되는 문제이다. Postfix 연산은 Stack 을 사용하면 쉽게 구현할 수 있다. 다만 본 문제에서 deque() 를 사용한 Stack 구현을 해야할지 List 를 사용한 Stack 구현을 해야할지 결정해야했다. 여기서 문제의 제약조건에서 tokens.length 는 1 부터 104 의 범위를 가지는 것을 볼 수 있는데, 이러한 상황에서는 deque 보다는 stack 으로 구현하는 것이 더 적절하다고 판단했다. 그렇게, List 로 Stack 를 구현하여 연산 순서도 중요하기에 first item 은 fi, second item 은 si 로 변수로 따로 설정하여 적절한 순서대로 pop 하여 연산 및 연산된 값을 다시 push ( append ) 하여 뒤의 연산까지 연결되게 구현했다. append() 및 push() 는 O(1) 의 시간복잡도를 가지나, 모든 아이템을 조회한다는 점에서 결론적으로 O(n) 의 시간복잡도를 가진다. 또한, 별도의 stack List 가 생성되고 있다. 다만 제약조건때문에 숫자 token 이 계속 n 번 들어오지는 않겠지만, 이론적인 upper boundary 는 일차식인 n 에 대하여 표현되기 때문에, 개수와 상수항이 무시된 O(n) 이 설정되게 된다.

-   **접근 2**
  - 속도의 개선을 위하여 fi 와 si 부분에 변화를 조금 주었다. 나누기와 빼기 부분은 값의 위치가 결과에 영향을 주는 요소이다. 하지만 곱셈과 덧셈은 그렇지 않다. 그렇기에 곱셈 부분과 덧셈부분은 fi 와 si 를 엄격하게 설정하여 값을 계산하는게 아닌 단순히 pop 하여 연산하도록 하여 불필요한 값의 저장과 저장된 값을 불러와 연산하는 부분을 최소화하였다. list의 token 을 처리하는 조회 로직은 접근 1번과 동일하기에, 시간복잡도와 공간복잡도는 접근 1번과 동일하게 O(n) 의 공간복잡도와 시간복잡도를 가진다.

### 📝 추후 개선점

- 나눗셈 부분에서 math.trunc() 가 아닌 int() 를 통하여 내부 함수 사용으로 해결할 수 있다는 점과, 오히려 미세하게 빨라질 수 있는 요소가 존재한다. 똑같은 기능을 하더라도 이러한 미세한 속도 차이가 날 수 있는 요소라도 기억하고 있어야 할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                si = stack.pop()
                fi = stack.pop()
                stack.append(fi + si)
            elif item == '-':
                si = stack.pop()
                fi = stack.pop()
                stack.append(fi - si)
            elif item == '*':
                si = stack.pop()
                fi = stack.pop()
                stack.append(fi * si)
            elif item == '/':
                si = stack.pop()
                fi = stack.pop()
                stack.append(math.trunc(fi / si))
            else: #숫자 입력일때
                stack.append(int(item))
        return stack[0]
```

```python
#풀이 2 (Stack Optimized)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                stack.append(stack.pop() + stack.pop()) #순서가 필요없는 + 연산에서는 si, fi 따로 저장하지 않는 방식으로 최적화
            elif item == '-':
                si = stack.pop()
                fi = stack.pop()
                stack.append(fi - si)
            elif item == '*':
                stack.append(stack.pop() * stack.pop()) #순서가 필요없는 * 연산에서는 si, fi 따로 저장하지 않는 방식으로 최적화
            elif item == '/':
                si = stack.pop()
                fi = stack.pop()
                stack.append(math.trunc(fi / si))
            else: #숫자 입력일때
                stack.append(int(item))
        return stack[0]
```

### 🤔 고찰

- Stack 의 구현을 위하여 어떤 방식을 사용할까? 라는 고민에 문제의 제약조건을 사용한 문제였다. 평소 문제를 풀때 이번 문제에서 그랬던것 처럼 제약조건을 상세하게 파악 및 이용한 경우는 크지 않았던 것 같다. 제약조건 덕분에 문제를 맞출 수 있는 경우가 생길 수 있지만 오히려 제약조건 때문에 문제를 틀릴 수도 있다는 점에서 제약조건을 잘 파악하는 습관을 들여놔야 할 것이다.
