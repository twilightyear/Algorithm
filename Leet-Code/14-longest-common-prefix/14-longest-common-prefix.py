class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: #입력값이 비어있다면 굳이 연산과정 생략하고 바로 반환
            return ""

        strs.sort() #입력 리스트 정렬. 정렬해서 첫값과 마지막 값만 비교
        
        first = strs[0]
        last = strs[-1]

        ptr = 0 #이동 포인터로 편하게 조회

        while(ptr<len(first) and ptr<len(last)): #ptr이 첫 값과 마지막 값 전부 마지막에 도달할 때 까지 이동
            if first[ptr] != last[ptr]: #다르면 루프를 종료
                break
            
            ptr+=1
        return first[:ptr]
