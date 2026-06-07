class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while(left>=0 and right<=len(s)-1 and s[left]==s[right]): #확장 조건
                left-=1
                right+=1
            return s[left+1:right] #여기까지 도달했다는 것은 확장조건에 위배되었다는 의미다. 그러므로 이전의 포인터를 반환한다.

        result="" #초기값

        for i in range(len(s)): #0부터 s의 길이+1 만큼 순회한다.
            even = expand(i,i) #홀수라고 가정하고 탐색
            odd = expand(i,i+1) #짝수라고 가정하고 탐색
        
            result = max(result,even,odd,key=len) #길이가 가장 긴 값을 저장
        
        return result
