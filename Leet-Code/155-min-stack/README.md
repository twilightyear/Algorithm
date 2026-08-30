### [ LeetCode ] 155. Min Stack

### 📌 문제 링크

[LeetCode - Min Stack](https://leetcode.com/problems/min-stack/description/)

### ⚠️ 제약조건

- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

### 🛠️ 풀이 접근 및 분석

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

> Implement the MinStack class:

> MinStack() initializes the stack object.
> void push(int value) pushes the element value onto the stack.
> void pop() removes the element on the top of the stack.
> int top() gets the top element of the stack.
> int getMin() retrieves the minimum element in the stack.
> You must implement a solution with O(1) time complexity for each function.

-   **접근 1**
  - 본 문제는 단순히 Stack 을 구현하는 문제처럼 보인다. 하지만 본 문제의 쟁점은 getMin() 함수에 존재한다. 문제에서는 모든 문제의 시간복잡도를 O(1), 즉 모든 함수에 대하여 일정한 시간에 실행되는 성능을 원한다. 그렇기에 단순히 기존에 전통적으로 사용하던 최소값 구하는 알고리즘은 O(n) 이므로 사용할 수 없을 것이다. 그렇기에 이 문제가 필요로하는 메인 stack 구현용 arr 과 함께 min 저장용 arr 를 사용하여 push 혹은 pop 과정에서 바로바로 min 을 계산하여 저장하는 방법이 최선이라고 판단했다.
  - 과정은 상당히 단순하다. push 먼저 생각해보자. 먼저 하나의 값이 push 되었다고 생각해보자. 만약 stack의 길이가 0이라면, 즉 이것이 첫 값이라면 따로 논리적으로 계산할 것도 존재하지 않으니, stack arr 과 min arr 에 추가해준다. 이후 과정이 중요하다. 이후에는 값이 들어왔을때 stack 에 추가하는건 동일하되, 해당 값이 min arr 의 top 값과의 크기비교를 통하여 같거나 작은 경우에만 min arr 에 append 하여 최신화를 함과 동시에 이전에 있었던 min 값까지 저장하는 역할을 하게 할 수 있다. 여기서 getMin() 함수를 사용하면 단순 min 의 top 값을 추출 하는 것으로 현재값까지의 최소값을 정상적으로 추출 할 수 있다.
  - 다음은 pop 을 생각해보자. pop 에서는 stack 의 top 값을 먼저 꺼내고 삭제한다는 가벼운 논리는 먼저 실행한다. 이때 꺼내진 값과 min 스택의 top 값을 비교하는 과정이 필요하다. 동일하다면, 최대값이 이제 사라진다는 것과 동일한 의미이다. min 스택 또한 pop 을 하여 top 값을 삭제한다. 여기서 push 에서 min arr 의 top 값과 크기 비교를 통하여 같거나 작은 경우만 append 했던 이유를 잘 이해할 수 있다. 예를들어 3 이라는 min 의 top 값이 있었을때 3 이 또 들어올때 중복이라고 추가를 안하는 것이 아니라 추가를 해주어야만 만약 3이 pop 된다고 min 에서의 3을 지우게 되었을때 stack 에서 아직 존재하는 3에 대하여 대응되는 3이 남아있을 수 있게 된다.
  - 위의 과정에서는 min 스택은 애초에 만들어지는 원리상 중복이 존재하는 값에 대한 내림차순으로 설정이 되기에, pop 과정에서 발생할 수 있다고 생각하는 여러 모순점들은 위의 내림차순이라는 특성 덕분에 문제가 발생하지 않으며 오히려 논리적으로 작동할 수 있게 된다.

### 📝 추후 개선점

-  push() 함수의 if self.min[-1] >= value: 부분에서 >= 부분에 있어서 > 으로 두고 해결하기 위하여 상당한 시간을 투자했다. 이러한 논리적인 부분에 있어서 사고력 증진에 있어서 아직 공부와 노력이 필요한 것 같다... 

### 💻 풀이 코드

```python
#풀이 1 (Stack)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if (len(self.stack) > 1):
            if self.min[-1] >= value:
                self.min.append(self.stack[-1])
            else:
                pass
        else:
            self.min.append(self.stack[-1])

        

    def pop(self) -> None:
        value = self.stack.pop()
        if self.min[-1] == value:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
```


### 🤔 고찰

- 문제를 처음 마주했을때, 이런 쉬운문제가 있나 싶어서 가벼운 마음으로 도전을 했다. 하지만 getMin() 함수를 구현하면서 발생하는 O(1) 의 min 구하는 로직에 대한 고민과 이해에 오랜 시간이 걸렸던 것 같다. min 을 빠르게 구하기 위해서 사실 min 스택에 저장하는 논리는 결국 시간-공간 트레이드오프 관계라는 것과 관련이 큰 것 같다. 이러한 점을 명심하자.
