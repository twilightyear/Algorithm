#풀이 1 (Queue)

from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    result = []
    s = []
    
    for i in range(len(progresses)): #몇 일 걸리는지 기능별로 계산
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    while days:
        day = days.popleft()
        if s:
            if s[0] >= day:
                s.append(day)
            else:
                result.append(len(s))
                s = [day]
        else:
            s.append(day)
    
    if s:
        result.append(len(s))
        
    return result
