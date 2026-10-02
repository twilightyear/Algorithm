# 풀이 1 (Queue)
from collections import deque

def solution(priorities, location):
    queue = deque([(p,i) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        proc = queue.popleft()
        
        if any(proc[0] < q[0] for q in queue):
            queue.append(proc)
        else:
            count += 1
            if proc[1] == location:
                return count
