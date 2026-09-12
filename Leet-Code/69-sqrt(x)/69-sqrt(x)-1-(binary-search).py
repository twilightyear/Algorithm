#풀이 1 (Binary Search)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while(left < right):
            mid = left + (right - left + 1) // 2
            power = mid*mid

            if(power < x):
                left = mid
            elif(power > x):
                right = mid - 1
            else:
                return mid

        return right
