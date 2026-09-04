### [ LeetCode ] 74. Search a 2D Matrix

### 📌 문제 링크

[LeetCode - Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

### ⚠️ 제약조건

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -104 <= matrix[i][j], target <= 104

### 🛠️ 풀이 접근 및 분석

> You are given an m x n integer matrix matrix with the following two properties:

> Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

> You must write a solution in O(log(m * n)) time complexity.

-   **접근 1**
 - 문제에서 O(log(m * n)) 의 시간복잡도 내에서 문제가 실행되기를 원하고 있다. log(m * n)은 log m + log n 이다. 여기서 m 개의 row 가 존재하고 n 개의 col 이 존재한다라고 한 문제 특성상, row 를 특정하기 위해 log m 의 시간복잡도를 가지는 이분탐색 1회, log n 의 시간복잡도를 가지는 이분탐색 1회 이렇게 시행하여 코드를 구성하면 제약조건 내로 문제를 해결할 수 있다고 판단했다. 하지만 row 를 특정할때 row 의 첫번째 값으로 정한다고 할때, target 값과 같은 경우도 있겠지만, 오히려 다른 경우가 더 많다. 그렇기에 target 값이 해당하는 범위를 가지도록 row 를 설정해야 했는데, mid 를 구하는 것은 루프문 이전에 두어서 최초설정을 하고, 한번의 비교문을 통하여 right 와 left 를 이동 후 mid 를 갱신하는 방법으로, 범위를 반환하는 과정에서 가장 최신화된 mid 를 반환할 수 있게끔, return 이전에 갱신하는 방법을 선택했다.
 - 이렇게 적절한 row 가 선택된 상황에서 전통적인 이분탐색을 col 에 사용하면 문제를 해결할 수 있었다.

### 📝 추후 개선점

- 만약 target 값이 첫번재 row 의 첫 값보다 작은 값이 들어오게 된다면, mid 가 -1 가 반환되어 col_idx_search() 에서 원하지 않은 마지막 행에 대하여 이분 탐색을 하는 상황이 생길 수 있었다. 물론 해당 행에 존재하지 않는 원소이기도 하고, 첫째 행의 첫값, 즉 모든 값보다 작은 값이라 동일하게 False 가 반환되어도 문제없긴 하지만, 의도대로 전부 작동하지 않은 경우라고 할 수 있다. 물론 이것까지 설계되어서 굳이 예외처리를 할 필요가 없다고 판단을 미리 했다면 크게 상관은 없었겠지만, 의도한게 아닌 코드인 만큼, 만약 코드가 조금이라도 다른 로직이였으면 틀린 결과를 반환하게 되었을 것이다. 이러한 엣지 케이스들에 대하여 꼼꼼하게 살펴보는 습관을 들여야 할 것이다.

### 💻 풀이 코드

```python
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
```

### 🤔 고찰

- 이 문제를 푼 다른 사람들의 풀이를 살펴보니 정말 감명받았던 풀이들이 몇 존재했다. 바로 하나의 행에 있는 데이터들보다 뒤의 행에 있는 데이터들의 크기가 더 크면서, 한 행에서는 오름차순으로 이루어져있다라는 특성을 활용한 1차원 배열로의 전환이다. 물론 직접 1차원 배열로 배열을 다시 선언하고 만드려면 O(log(n*m)) 으로 풀 수는 없다. 하지만, 따로 만들지 않고, 2차원 배열을 1차원 배열로 취급해서 // 와 % 연산자를 이용해서 몫과 나머지를 활용하여, 내가 했던 풀이와는 다르게, 한번의 이분탐색으로도 풀이가 가능했다.
- 또한 다른 방식으로는, 바둑판 위의 바둑돌을 움직이듯, 한번에 가로, 한번에 세로가 아닌, 조건에 따라서 옆으로 움직이고, 아래로 움직이는 방식으로 조작하여 정답을 도출하는 방식을 적용한 풀이도 살펴보았다. 코드가 이분탐색으로 작동하는 것이 아닌, 오히려 투 포인터에 가깝기에, O(m+n) 이라 시간초과가 나긴 하겠지만, 이러한 접근법도 존재한다는 것을 배웠다.
