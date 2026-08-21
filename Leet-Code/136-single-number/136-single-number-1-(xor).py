#풀이 1 (Xor)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for item in nums:
            result^=item #Xor 연산
        return result
