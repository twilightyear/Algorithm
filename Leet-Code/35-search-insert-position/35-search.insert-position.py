class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        left=0 #초기 양 끝값을 설정한다.
        right=len(nums)-1

        #아주 정석적인 이분탐색법이다.
        while(left<=right):
            mid = left+(right-left)//2 #오버플로우 발생 가능성을 고려하여 mid를 계산한다.

            if(nums[mid]>target):
                right = mid-1
            elif(nums[mid]<target):
                left = mid+1
            else:
                return mid
        #본 문제에서 만약 같은 요소가 없으면 "정렬"이라는 조건이 있으니 단순하게 left를 반환하면 된다.
        return left
