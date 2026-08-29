#풀이 1 (Bruteforce)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            found=False
            
            for j in range(i,len(temperatures)):
                if(temperatures[j]>temperatures[i]): #처음 커지는 값을 만나면 해당 값 추가
                    result.append(j-i)
                    found=True
                    break

            if not found:
                result.append(0) #못찿았다면 0 추가
        
        return result
