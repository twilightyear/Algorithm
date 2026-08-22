#풀이 1 (Set)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest=0

        for num in nums_set:
            if num-1 not in nums_set: #num 보다 1 작은, 즉 num이 연속적 부분의 첫 값 후보로 설정한다.
                length = 1
                while num+length in nums_set: #뒤에 연속적 값이 계속 나오면 length 를 증가시킨다.
                    length+=1
                
                longest = max(length,longest) #값 최신화

        return longest
