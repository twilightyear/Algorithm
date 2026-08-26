#풀이 1 (Two Pointer)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_arrs = []
        nums.sort()

        for i in range(0,len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i>0 and nums[i] == nums[i-1]: #nums[i] 에 대한 중복방지
                continue

            while(left<right):
                tsum = nums[left]+nums[right]+nums[i]

                if(tsum > 0):
                    right-=1
                elif(tsum < 0):
                    left+=1
                else:
                    result_arrs.append([nums[i],nums[left],nums[right]])

                    while(left<right and nums[left]==nums[left+1]): #nums[left] 에 대한 중복방지
                        left+=1
                    while(left<right and nums[right]==nums[right-1]): #nums[right] 에 대한 중복방지
                        right-=1
                    
                    right-=1
                    left+=1

        return result_arrs
