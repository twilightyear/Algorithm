### [ LeetCode ] 36. Valid Sudoku

### 📌 문제 링크

[LeetCode - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

### ⚠️ 제약조건

- **board.length == 9**
- **board[i].length == 9**
- **board[i][j] is a digit 1-9 or '.'.**

### 🛠️ 풀이 접근 및 분석

> Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

> Each row must contain the digits 1-9 without repetition.
> Each column must contain the digits 1-9 without repetition.
> Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

> A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

-   **접근 1**
    - 본 문제는 생각보다 단순하다. 스도쿠가 풀수 있는지 여부까지 볼 필요가 전혀 없으며, **가로** **세로** , 그리고 **3x3 박스** 내부마다 **1~9** 의 숫자 중에서 중복된 값이 있는지의 여부만 파악하면 마무리 되는 문제이다. 바로 생각나는 풀이이며 가장 직관적인 풀이인 가로를 기준으로 **Set** 을 통하여 중복확인을 빠르게 확인하고, 세로를 기준으로 동일한 방법으로 확인하며, 마지막으로 **3x3** 영역들을 대상으로 동일한 방식으로 확인한다. 스도쿠의 크기가 정해져있음으로 **Set** 과 **Bruteforce**를 사용한 방식에도 불구하고 **O(1)** 의 시간/공간복잡도를 가지게 적용 가능할 것이라는 생각에 풀이를 해보았다.

### 📝 추후 개선점

-  풀이를 제출하고 보니 바로 상위권의 속도를 보였으며, 다른 상위권 코드들과 비교해보니 결국 풀이 논리는 동일했다. 중복요소를 잡기 위하여 **Set** 을 사용하며, **가로** 와 **세로** , 그리고 **3x3** 영역을 동일한 논리로 모든 요소를 확인하는 과정은 불가피했다.
- 아무튼 접근법은 동일했으나, 최적화의 여부는 아니다. 본 코드보다 더 빠르게 작동하는 코드를 살펴보니 **3번** 따로 순회하는 것은 맞으나, 한번의 **for** 루프에서 작동하여 조금이라도 더 빠르게 연산하는 경우를 살펴보았다. 풀이 코드에서

```python
        for i in range(9):
            row = set([])
            for j in range(9):
```

위와같은 동일한 부분이 **3번** 따로 사용된다는 사실을 알 수 있다. 이러한 동일한 부분을 한번에 압축하여 불필요한 연산을 줄일 수 있다는 것이다.


### 💻 풀이 코드

```python
#풀이 1 (Bruteforce)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9): #가로 확인
            row = set([])
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                row.add(board[i][j])

        for i in range(9): #세로 확인
            col = set([])
            for j in range(9):
                if board[j][i] != "." and board[j][i] in col:
                    return False
                col.add(board[j][i])
        
        for i in range(0,9,3): #3x3 확인
            for j in range(0,9,3):
                cube = set([])
                for k in range(i,i+3,1):
                    for l in range(j,j+3,1):
                        if board[k][l] != "." and board[k][l] in cube:
                            return False
                        cube.add(board[k][l])

        return True
```


### 🤔 고찰

- **중복요소** 하면 **Set** 을 떠올리고, 마땅히 더욱 효율적인 해결방식이 떠오르지 않아 일단 **Bruteforce** 를 적용하여 풀어본 접근법이 뭔가 이전의 자신보다 나아진 것 같아 실력향상이 이루어지고 있다는 느낌이 들어서 약간 뿌듯한 느낌이 들었던 문제풀이 시간이였다. 이러한 무엇 하면 무엇으로 접근해야겠다 라는 경험과 직관력을 기르는 시간이 더 쌓여 정말 효율적으로 코드를 짜내는 개발자가 되야겠다.
