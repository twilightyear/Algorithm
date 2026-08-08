#풀이 2 (Dictionary & Heap(Priority Queue))
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        priority_queue=[]
        result=[]
        heapq.heapify(priority_queue)

        for num, freq in collections.Counter(nums).items(): #Dictionary 를 이용한 Counter
            heapq.heappush(priority_queue, (-freq,num)) #우선순위를 음수화 하여 역우선순위로 저장

        for i in range(k):
            result.append(heapq.heappop(priority_queue)[1]) #우선순위가 높은, 즉 음수를 취하기 전의 의미로는 우선순위가 낮은 원소들을 추출
        
        return result
