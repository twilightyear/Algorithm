#풀이 1 (Bruteforce)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(1,max(piles)+1): #가능한 k 값 전부 조회

            hours = 0
            for i in range(len(piles)): #k 값에 대한 걸리는 시간 확인
                hours += math.ceil(piles[i]/k)
            
            if(hours == h):
                return k
