#풀이 2 (Optimized)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1]*length #오버헤드 개선을 위한 크기 및 Array 사전 설정

        forward=1
        for i in range(length): #전진부분 계산 및 설정
            result[i]=forward
            forward*=nums[i]

        backward=1
        for j in range(length-1,-1,-1): #후진부분 계산 및 곱하기
            result[j]*=backward
            backward*=nums[j]

        return result
