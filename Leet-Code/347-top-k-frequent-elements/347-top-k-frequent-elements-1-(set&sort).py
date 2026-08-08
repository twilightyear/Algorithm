#풀이 1 (Set & Sort)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = set(nums)
        arr = []
        result = []

        for item in data: #유일한 원소들에 대하여 [[개수],[원소]] 의 형식으로 저장
            arr.append([nums.count(item),item])

        arr.sort(reverse=True) #내림차순 정렬

        for i in range(k):
            result.append(arr[i][1]) #k개만큼 앞에서 추출

        return result
