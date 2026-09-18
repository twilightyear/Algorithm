# 풀이 2 (Sliding Window & Array)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False

        s1_c = [0]*26
        w_c = [0]*26

        for char in range(l1):
            s1_c[ord(s1[char]) - ord('a')] += 1
            w_c[ord(s2[char]) - ord('a')] += 1

        if(s1_c == w_c):
            return True

        for i in range(l1, l2):

            w_c[ord(s2[i]) - ord('a')] += 1
            w_c[ord(s2[i-l1]) - ord('a')] -= 1

            if(s1_c == w_c):
                return True

        return False
