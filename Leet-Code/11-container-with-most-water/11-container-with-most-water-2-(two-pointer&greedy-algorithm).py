#풀이 2 (Two Pointer & Greedy Algorithm)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        while(left<right):
            area = min(height[left],height[right])*(right-left)

            if(height[left]>height[right]): #길이가 작아짐에 따라 높은 막대기가 아닌 작은 막대기를 포기
                right-=1
            else:
                left+=1

            max_area = max(max_area,area) #최대 넓이 갱신
 
        return max_area
