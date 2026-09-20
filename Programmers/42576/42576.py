# 풀이 1 (Hashmap)
from collections import defaultdict

def solution(participant, completion):
    m = defaultdict(int)
    answer = ""
    for person in completion:
        m[person] += 1
        
    for person in participant:
        if m[person] == 0:
            return person
        m[person] -= 1
