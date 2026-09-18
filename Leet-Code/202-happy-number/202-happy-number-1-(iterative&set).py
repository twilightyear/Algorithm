#풀이 1 (Iterative & Set)
class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num): 
            result = 0
            for digit in str(num):
                result += int(digit)*int(digit)
            return result

        visited = set()
        while(1):
            n = cal(n)

            if(n == 1):
                return True

            if(n in visited):
                print(n)
                return False
            else:
                visited.add(n)
