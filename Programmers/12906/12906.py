# 풀이 1 (Deque)
from collections import deque

def solution(arr):
    answer = deque()
    prev = None
    for i in arr:
        if prev != i:
            answer.append(i)
            prev = i

    return list(answer)
