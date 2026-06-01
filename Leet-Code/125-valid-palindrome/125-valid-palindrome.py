import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = re.sub("[^a-zA-Z0-9]","",s.lower()) #정규표현식을 사용하여 조건 처리 간결화
        if data == data[::-1]: #동작이 빠른 리스트 슬라이싱을 사용하여 reverse 비교
            return True
        else:
            return False
