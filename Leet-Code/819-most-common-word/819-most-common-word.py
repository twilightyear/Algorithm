import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = [word.lower() for word in re.sub("[^a-zA-Z0-9]"," ",paragraph).split() if word.lower() not in banned] #리스트 컴프리헨션. 조건에 맞게 주어진 데이터를 조작.

        return Counter(words).most_common(1)[0][0] #Counter에서 가장 value 값이 높은 key를 반환
