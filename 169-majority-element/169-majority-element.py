class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #정렬 진행 (Tim Sort)

        return nums[math.floor(len(nums)/2)] #정렬한 데이터 기준 중간에 있는 값은 무조건 최빈값의 영역이다.
