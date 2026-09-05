# 풀이 2 (Binary Search)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left<right):
            mid = left + (right - left) // 2

            if(nums[mid] > nums[right]): # 중간값인 mid 가 오른쪽보다 크다면 논리적으로 최솟값은 여기 사이에 존재함.
                left = mid + 1
            else: #중간값인 mid 가 오른쪽보다 작다면, 최솟값은 mid 이거나, 더 아래에 있음
                right = mid

        return nums[right]
