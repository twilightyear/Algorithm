#풀이 1 (Subtraction)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num_idx in range(len(numbers)):
            sub = target-numbers[num_idx] #뺀 값 구하기
            
            if sub in numbers:
                sub_idx = 0
                for j in range(len(numbers)): #뺀 값의 인덱스 확인 과정
                    if numbers[j] == sub:
                        sub_idx = j
                return [num_idx+1, sub_idx+1] #각각 1을 더한값을 반환
