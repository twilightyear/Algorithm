### [ LeetCode ] 130. Surrounded Regions

### 📌 문제 링크

[LeetCode - Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=breadth-first-search)

### ⚠️ 제약조건

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
  - 전통적인 BFS 알고리즘 접근법을 이용했다. 다만, 문제 특성상 결국 테두리에 인접한 O 가 아닌이상 무시해도 무관하니, 모든 board 의 O 를 보는 것이 아닌, 테두리의 O 만 보고 visited set 과 queue 에 추가해주고, 이후 queue 를 통한 전통적인 방문법을 통하여 테두리의 O 와 인접한 모든 O 에 방문해주며 visited set에 마찬가지로 표시한다. 마지막으로, 모든 board 를 조회하며, 해당 좌표를 visited 에 조회하고, 이를 바탕으로 O 라고 해도 visited 에 표기되지 않은 영역은 테두리로 나가지 못한, 즉 Surrounded Regions 라고 판단하여 X 로 표기를 교체해준다. 행의 개수 N 와 열의 개수 M 에 대하여 O(N * M) 의 시간복잡도와 공간복잡도를 가지게 된다.

### 📝 추후 개선점

- 따로 학습했던 BFS 문제를 풀어보는 시간을 가졌다. 나름 응용을 통하여 테두리만 queue 와 visited 에 추가한다는 생각은 좋았지만, 이 풀이 방식이 과연 Python 에서 쓸만할까라는 생각을 하게 되었다. 그래서 다른 풀이들을 찿아보니 큰 틀은 비슷했지만, visited set 을 사용하는 대신, board 자체에 "T" 라고 표기하며 방문했다라는 표시를 board 자체에 남겨 효율을 높히는 방안을 사용한것을 볼 수 있었다. 당분간 BFS 유형이 익을때까지 많이 풀어봐야겠다.

### 💻 풀이 코드

```python
#풀이 1 (Algorithm)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]

        visited = set()

        queue = deque([])

        n = len(board)-1
        m = len(board[0])-1

        for x in range(n+1): #세로
            for y in range(m+1): #가로
                if(x==0 or x==n) or (y==0 or y==m):
                    if(board[x][y] == "O"):
                        queue.append([x,y])
                        visited.add((x,y))
                
        while(queue):
            pair = queue.popleft()
            for i in range(4):
                X = pair[0] + dx[i]
                Y = pair[1] + dy[i]
                if X < 0 or X > n or Y < 0 or Y > m:
                    continue
                if (X,Y) in visited:
                    continue
                if board[X][Y] == "X":
                    continue
                visited.add((X,Y))
                queue.append([X,Y])

        for x in range(n+1): #세로
            for y in range(m+1): #가로
                if((x,y) not in visited and board[x][y] == "O"):
                    board[x][y] = "X"
```
