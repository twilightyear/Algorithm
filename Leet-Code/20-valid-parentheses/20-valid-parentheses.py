class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in dictionary: #닫는 기호일 경우

                if not stack: #stack이 비어있는 경우
                    return False

                if(stack.pop()!=dictionary[char]): #stack의 top 값과 char에 대응되는 여는 기호가 다른 경우.
                    return False

            else: #여는 기호일 경우
                stack.append(char)

        #stack이 비어있다면 잘 처리된것
        return len(stack) == 0
