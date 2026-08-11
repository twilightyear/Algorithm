#풀이 1 (Array)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_forward_arr = []
        product_backward_arr = []

        length = len(nums)

        for i in range(length): #앞에서부터 곱하는 Arr과 뒤에서부터 곱하는 Arr 각각 생성
            if i==0:
                product_forward_arr.append(nums[0])
                product_backward_arr.append(nums[-1])
            else:
                product_forward_arr.append(product_forward_arr[i-1]*nums[i])
                product_backward_arr.append(product_backward_arr[i-1]*nums[-(i+1)])

        product_backward_arr.reverse()

        result = []

        for j in range(length): #만들어둔 두 Arr 를 사용하여 Result 연산
            if j==0:
                result.append(product_backward_arr[j+1])
            elif j==length-1:
                result.append(product_forward_arr[j-1])
            else:
                result.append(product_forward_arr[j-1]*product_backward_arr[j+1])
        
        return result
