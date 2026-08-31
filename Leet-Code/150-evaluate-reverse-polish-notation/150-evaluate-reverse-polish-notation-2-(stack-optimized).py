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
