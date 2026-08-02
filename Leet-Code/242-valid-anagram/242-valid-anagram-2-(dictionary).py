#풀이 2 (Dictionary)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #길이가 다른 두 문자열이면 조건 성립불가
            return False

        dictionary = {}

        for element in s: #문자열 s 에 대하여 각 알파벳을 이용한 카운터
            if element not in dictionary:
                dictionary[element] = 1 
            else:
                dictionary[element] += 1
        
        for element in t: #문자열 t 에 대하여 카운터의 값 감소
            if element in dictionary:
                dictionary[element] -= 1

        for element in s: #문자열 s 대하여 다시 조회하여 카운터값이 전부 0 인 경우에만 True 반환
            if dictionary[element] != 0:
                return False
        return True
