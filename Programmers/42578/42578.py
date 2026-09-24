# 풀이 1 (Hashmap)
from collections import defaultdict

def solution(clothes):
    map = defaultdict(list)
    
    for cloth, category in clothes:
        map[category].append(cloth)
        
    answer=1
    for item in map:
        answer*=(len(map[item])+1)
        
    return answer-1
