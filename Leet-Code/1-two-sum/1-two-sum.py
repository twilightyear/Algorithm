class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        #[[기존값,기존인덱스]] 형태로 2차원 배열을 만든다.
        for i in range(len(nums)):
            answer.append([nums[i],i])

        #만들어진 배열을 [[기존값,기존인덱스]] 중에서 기존값 기준으로 정렬한다.
        answer.sort()

        #위에서 정렬한 배열에 Two Pointer를 사용해서 정답을 도출한다.
        #-> 인덱스에 해당하는 값과 target값의 비교를 통하여 left, right 값을 조작한다.
        left = 0
        right = len(nums) - 1
        while left < right:
            if answer[left][0] + answer[right][0] < target:
                left+=1
            elif answer[left][0] + answer[right][0] > target:
                right-=1
            elif answer[left][0] + answer[right][0] == target:
                return [answer[left][1], answer[right][1]]


        #정답을 반환한다.
        return answer
