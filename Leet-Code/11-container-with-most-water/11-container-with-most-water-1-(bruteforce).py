#풀이 1 (Bruteforce)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)

        for i in range(length-1):
            for j in range(length):
                area = min(height[i],height[j])*(j-i) #넓이 계산
                max_area = max(max_area, area)

        return max_area
