class Solution:
    def reverseString(self, s: List[str]) -> None:

        left=0 #투포인터가 가르킬 양쪽 끝을 초기화한다.
        right = len(s)-1

        while left<=right: #한번씩만 조회하면 됨으로 left<=right으로 반복문을 돌린다.

            tmp = s[left] #tmp를 사용하여 swap을 한다.
            s[left] = s[right]
            s[right] = tmp

            left+=1 #두개의 포인터들을 이동한다.
            right-=1
