class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        string = []
        number = []

        for log in logs: 
            log = log.strip() 
            if log.split()[1].isdigit(): #비식별자 부분이 숫자
                number.append(log)
            else: #비식별자 부분이 문자열
                string.append(log)


        string.sort(key=lambda x: (x.split()[1:], x.split()[0])) #문자열 부분만 정렬
        
        
        return string + number #순서에 맞게 연결해서 반환
