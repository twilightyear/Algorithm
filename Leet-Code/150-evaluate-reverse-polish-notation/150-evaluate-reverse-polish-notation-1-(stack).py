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
