class Solution:
    def reverse(self, x: int) -> int:

        #부호를 기억하고 절댓값으로 변환한다.
        sign=1
        if(x<0):
            sign=-1
            x=-1*x
        
        #문자열화 한 후 배열을 뒤집고 정수로 전환하고 부호를 다시 붙여준다. 
        result = int(str(x)[::-1])*sign

        #문제에서 제시한 범위의 숫자인지 확인한다.
        if(-2**31<=result and result<=2**31+1):
            return result
        else:
            return 0
