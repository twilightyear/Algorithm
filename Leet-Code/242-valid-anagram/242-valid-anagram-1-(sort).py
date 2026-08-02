#풀이 1 (Sort)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #정렬한 두 문자열을 비교
