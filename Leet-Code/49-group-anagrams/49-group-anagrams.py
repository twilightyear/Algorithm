class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {} #Hashmap 만들기

        for word in strs:
            sorted_word = ''.join(sorted(word)) #단어 먼저 꺼내고 알파벳 단위로 정렬
            if sorted_word not in hashmap: #hashmap에 없다면 리스트로 넣기
                hashmap[sorted_word] = [word] 
            else:
                hashmap[sorted_word].append(word) #hashmap에 있다면 append로 추가하기
          
        return list(hashmap.values()) #리스트로 values 반환. (정렬된 값은 필요없다.)
