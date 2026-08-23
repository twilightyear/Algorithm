#풀이 1 (Two Pointer)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 #투포인터 설정
        right = len(numbers)-1

        while(left<right):
            sum_tmp = numbers[left]+numbers[right]
            if(sum_tmp > target):
                right-=1
            elif(sum_tmp < target):
                left+=1
            else:
                return [left+1,right+1] #반환
