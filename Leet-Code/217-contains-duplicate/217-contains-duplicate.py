class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_data = set()

        for n in nums:
            if n in set_data: #데이터가 존재하는지 확인
                return True
            else:
                set_data.add(n)

        return False
