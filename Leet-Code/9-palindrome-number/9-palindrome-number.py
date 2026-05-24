class Solution:
    def isPalindrome(self, x: int) -> bool:

        #한번에 변환해놓음으로써 여러번 변환해야할 소요를 줄임.
        string = str(x)

        #뒤집은 문자열과 본래 문자열과 비교 : 같으면 True 반환, 다르면 False 반환
        if string==string[::-1]:
            return True
        else:
            return False
