#풀이 1 (Set)
def solution(nums):
    answer = 0
    chance = len(nums) / 2 #가져갈 수 있는 개수
    count = len(set(nums)) #총 종류
    
    if chance <= count: #가져갈 개수 보다 종류가 많다면
        return chance
    else: #가져갈 개수보다 종류가 적다면 총 종류 개수 반환
        return count
