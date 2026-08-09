class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=[]
        for string in strs:
            length = len(string)
            word = []
            for i in range(length):
                word.append(chr(ord(string[i])+length))
            encoded_str.append(str(length) + "@" + "".join(word))

        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        
        i=0
        while i<len(s):
            j=i
            while s[j]!="@": #시작지점부터 구분자까지 탐색
                j+=1

            length = int(s[i:j]) #길이부분

            i=j+1 #문자열 시작부분
            encoded_str = s[i:i+length] #문자열 부분
            
            word=[]
            for k in range(length):
                word.append(chr(ord(encoded_str[k])-length))
            decoded_strs.append("".join(word))

            i+=length #다음 지점으로 이동

        return decoded_strs
