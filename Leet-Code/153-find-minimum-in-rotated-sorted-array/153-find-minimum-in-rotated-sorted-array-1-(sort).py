# 풀이 1 (Sort)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()

        return nums[0]
