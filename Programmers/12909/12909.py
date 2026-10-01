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
