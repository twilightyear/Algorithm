### [ LeetCode ] 238. Product of Array Except Self

### 📌 문제 링크

[LeetCode - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

### ⚠️ 제약조건

- **2 <= nums.length <= 105**
- **-30 <= nums[i] <= 30**
- **The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.**

### 🛠️ 풀이 접근 및 분석

> **Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].**

> **The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.**

> **You must write an algorithm that runs in O(n) time and without using the division operation.**

-   **접근 1**
    - 처음 문제를 읽으면, 나눗셈을 사용한다면 정말 쉽게 풀 수 있을것 같다. 다만 **0** 으로 나누는 경우만 예외처리 하게 된다면 정말 편하게 풀 것 같았다. 하지만 문제 마지막줄에서 이러한 나눗셈을 사용한 너무나 쉬운 방식은 사용하지 말라고 지정을 해버린다.
    - 그렇기에 생각이 든 풀이법은 다음과 같다. 앞에서부터 곱하여 저장하고 뒤에서부터 곱하여 저장하는 방식으로 **2개** 의 별도의 **Array** 를 생성 및 저장한다. 이후 이 두 데이터들을 사용하여 **result Array** 에 값을 계산 및 추가하는 방식으로 진행한다면 위에서 앞에서부터 곱하여 저장하는 방식에서 **O(N)** 의 시간복잡도와 공간복잡도, 이후 독립적으로 다시 시행되는 뒤에서부터 작동하는 방식에 의해 동일하게 **O(N)** 의 시간/공간복잡도를 가지게 된다. 이후 또다시 독립적으로 **result Array** 에 한번씩 조회하며 계산 및 **Append** 를 진행하며 **O(N)** 의 시간및 공간복잡도를 가지며, 
    - 결론적으로 계수를 제거한 최고차항만 고려한 **O(N)** 의 시간복잡도와 **O(N)** 의 공간복잡도를 가지는 코드로 구성했다.
-   **접근 2**
    - **Leet Code** 의 다른사람들의 풀이와 비교한 성능평가를 보았을때 상당히 낮은 점수가 기록되었다. 본 접근 방식이 정말 최선의 방법일까를 고민하며, 결국 접근방식을 바꾸기보다는 코드의 최적화에 중점을 두어 다시 시도해보기로 했다.
    - **접근 1번** 의 코드는 **result Array** 의 계산을 위하여 **result** 이외에도 **2개** 의 추가 **Array** 를 생성 및 사용한다. 게다가 하나의 **Array** 는 **reverse** 를 사용하여 상당히 무겁게 작동한다. 여기서 수많은 **Append** 와 같은 요소들 때문에 상당한 오버헤드가 발생하여 이에 따른 성능 저하가 발생했다고 판단하여 이를 개선하는 방향으로 최적화 방식을 구체화했다. 이해를 위하여 사진을 사용하겠다.
    - **1번 접근** 에서 기존 방식이 아래와 같았다.
    - 
    <img width="321" height="282" alt="238  Product of Array Except Self drawio" src="https://github.com/user-attachments/assets/3fe509eb-fb24-4d8c-b3df-0553fda8dbe0" />

    - 하지만 **2번 접근** 에서는 방식이 아래와 같이 단순해졌다. 

    <img width="321" height="282" alt="238  Product of Array Except Self drawio (1)" src="https://github.com/user-attachments/assets/52927b7d-4c99-4a7d-9e61-9bc739fbda87" />

    
    - 정말 의미없던 과정의 축소라고 생각하면 편하다. 굳이 예외처리까지 해가며 **j-1** 인덱스와 **j+1** 를 비교하며 계산할 필요가 전혀 없었던 것이다. 그냥 전진 방식과 후진 방식을 위의 방식처럼 세팅하고 단순하게 곱하면 정답이 도출된다.

### 📝 추후 개선점

-  문제에서 제한한 사항을 이해하고 올바른 접근법을 통하여 문제를 풀이한 점은 참 좋았으나 결국 상당히 비효율적인 풀이였다. 다른 언어였으면 모르겠는데 파이썬을 사용한 풀이 코드였기에 이전 코드에서도 항상 말했듯, 오버헤드와 같은 요소들을 항상 경계했어야했다. 이외에도 그림을 통해서도 설명했듯, 조금만 풀이방식에 변화를 가하면 정말 아름답고 깔끔하게 계산이 되는데, 그러한 점을 눈치채지 못하고 말 그대로 구현해버려서 아쉬웠다. 한마디로 접근법은 좋았으나 풀이법은 아쉬웠던 경우의 풀이였다. 다음에는 좀 더 문제에 파고들어 개선점이 없나 시각적으로 종이에 그려보며 조금 더 깔끔하게 풀 수는 없을까 하는 사유의 과정이 있어야 할 것이다.

### 💻 풀이 코드

```python
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
```

```python
#풀이 2 (Optimized)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1]*length #오버헤드 개선을 위한 크기 및 Array 사전 설정

        forward=1
        for i in range(length): #전진부분 계산 및 설정
            result[i]=forward
            forward*=nums[i]

        backward=1
        for j in range(length-1,-1,-1): #후진부분 계산 및 곱하기
            result[j]*=backward
            backward*=nums[j]

        return result
```


### 🤔 고찰

- 생각보다 재미있게 풀었던 문제였다. 문제 풀이를 마치고 상위 점수를 기록한 코드를 살펴보니 많은 상위권 풀이가 문제에서 금지한 나눗셈 방식을 사용하고 있었다. 정말 실소가 터져나왔던 것 같다. 분명 고심해서 만든 풀이가 무슨 **Bruteforce** 로 만든 **O(N^2)** 풀이마냥 쓰레기 코드처럼 평가받으니 내가 이정도로 접근법이 별로인가 생각했었던 자신을 돌아보니 정말 웃겼다. 이렇게 **Leet Code** 에서도 제약사항에  특정 풀이법을 사용하지말라고 적어놓긴 했지만 사실상 크게 막을 방법이 없을 것이다. 그렇기에 나도 이러한 요상한 풀이법을 남기지 않게라도 문제와 제약조건을 항상 꼼꼼히 읽어야겠다는 생각을 했다.
