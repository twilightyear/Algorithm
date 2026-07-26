#풀이 1 (String 이용)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            
        result=0
        v = bin(n)[2:] # 이진수로 변환
        for i in range(len(v)):
            result+=int(v[i]) # 값 더하기
        
        if result==1: # 더한 값이 총 1이면 참 반환
            return True
        else:
            return False
