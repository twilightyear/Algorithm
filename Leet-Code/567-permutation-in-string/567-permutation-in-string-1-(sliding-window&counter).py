# 풀이 1 (Sliding Window & Counter)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        left = 0
        right = len(s1) - 1

        if(len(s1) > len(s2)): #s1 가 s2 보다 긴 경우 바로 False 반환
            return False

        while(right<len(s2)): #Sliding Window 를 조작하며 Permutation 확인
            c2 = Counter(s2[left:right+1])

            if(c2 == c1):
                return True

            left+=1
            right+=1

        return False
