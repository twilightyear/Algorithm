#풀이 2 (Bit 연산 이용)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and n&(n-1)==0: #양수거나 n의 이진수가 1이 1개를 넘어서 존재하지 않음
            return True
        else:
            return False
