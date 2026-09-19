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
