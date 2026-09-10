# 풀이 1 (Binary Search)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        #최소값의 index 탐색
        while(left < right):

            min_idx = left + (right - left) // 2
            if(nums[min_idx] > nums[right]):
                left = min_idx + 1
            else:
                right = min_idx

        pivot = left

        #범위에 따라 left right 값 설정
        if pivot == 0: #만약 단순 정렬된 형태라면
            left = 0
            right = len(nums)-1
        elif nums[pivot] <= target and target <= nums[-1]: #최소값 <= target <= 마지막원소 이라면
            left = pivot
            right = len(nums)-1
        else:
            left = 0
            right = pivot-1

        #다시 Binary Search
        while(left <= right):
            mid = left + (right - left) // 2

            if(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] == target):
                return mid
            
        return -1
