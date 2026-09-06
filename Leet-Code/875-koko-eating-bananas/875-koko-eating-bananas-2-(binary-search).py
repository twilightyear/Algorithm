#풀이 1 (Binary Search)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while(left<=right):

            mid = left + (right - left) // 2 #K 값에 대한 Binary Search

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            
            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return ans
