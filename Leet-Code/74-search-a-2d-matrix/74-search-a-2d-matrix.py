#풀이 1 (Binary Search & Boundary Search Pattern)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def row_idx_search(matrix, target): #Row 찿기
            left = 0
            right = len(matrix)-1

            mid = left + (right-left) // 2

            while (left<=right):

                if(matrix[mid][0] < target):
                    left = mid + 1
                elif(matrix[mid][0] > target):
                    right = mid - 1
                else:
                    return mid
            
                mid = left + (right-left) // 2
            return mid

        def col_idx_search(matrix, target): #정해진 Row 에 대하여 Col 찿기
            left = 0
            right = len(matrix)-1

            while (left<=right):

                mid = left + (right-left) // 2

                if(matrix[mid] < target):
                    left = mid + 1
                elif(matrix[mid] > target):
                    right = mid - 1
                else:
                    return True
            
            return False

        row = row_idx_search(matrix, target)
        return col_idx_search(matrix[row],target)
