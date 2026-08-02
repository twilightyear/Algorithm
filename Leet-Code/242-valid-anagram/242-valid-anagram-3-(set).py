#풀이 3 (Set)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #길이가 다른 두 문자열이면 조건 성립불가
            return False

        for i in set(s): #중복되지 않은 문자열 s 의 각 알파벳 원소들에 대하여 두 문자열 별도로 count 하고 비교
            if s.count(i) != t.count(i):
                return False
        return True
