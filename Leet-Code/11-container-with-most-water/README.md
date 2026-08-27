### [ LeetCode ] 11. Container With Most Water

### 📌 문제 링크

[LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

### ⚠️ 제약조건

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

### 🛠️ 풀이 접근 및 분석

> You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

> Find two lines that together with the x-axis form a container, such that the container contains the most water.

> Return the maximum amount of water a container can store.

> Notice that you may not slant the container.

 

-   **접근 1**
  - 문제를 처음 접근했을때 투포인터가 바로 생각이 나긴 했지만, 정렬이 되어있지도 않으며, 문제가 원하는 답을 구하기 위해서는 두 막대간의 길이도 무조건 필요한 값이니 정렬도 옳지 않다고 생각했지에 일단 Bruteforce 를 사용해서 풀이해보고 접근 방식을 개선해보겠다고 생각했다. 그렇게 i 의 범위와 j 의 범위를 적절히 설정하여 for 문을 통한 조회 및 넓이 값을 연산하여 최대넓이값을 갱신하여 마지막에 반환하도록 구성했다. 역시나 통과가 되지 않았다.추가적인 공간 사용은 다른 추가적인 값들이 쌓이지 않는 변수값의 사용만 있었기에 O(1) 의 공간복잡도를 가지나, 두개의 for 문을 사용하기에 O(N^2) 의 시간복잡도를 가지기 때문이다. 다시 다른 접근법을 생각해볼 필요가 있다.

-   **접근 2**
  - 기존에 생각했던 투 포인터를 사용할 수 있는 방법을 생각해냈다. 본 문제는 두 막대의 각 높이와, 막대 사이의 거리를 통하여 구할 수 있는 넓이의 최대치를 구하는 문제이기 때문에, 투포인터를 통한 이동 과정에서 막대 사이의 길이가 필연적으로 줄어들 수 밖에 없다면 높이를 포기해야한다는 결론을 도출 할 수 있다. 이때 두 막대 중에서 하나를 포기해야한다면 작은 막대를 포기해야 할 것이다. 이때 N 개의 막대 개수에 대하여 N번만 포인터를 움직이기 때문에, O(N)의 시간복잡도를 가지며, 접근 1번과 동일한 이유로 O(1) 의 공간복잡도를 가진다. 
  이렇게 Greedy Algorithm 을 적용하여 투포인터 코드를 구성하여 문제를 풀 수 있었다.

### 📝 추후 개선점

- 풀이 2번의 max() 함수의 사용에 있어서,

```python
max_area = max(max_area,area) #최대 넓이 갱신
```

가 아닌,

```python
if area > max_area: #최대 넓이 갱신
  max_area = area
```

를 사용한다면, 발생할 수 있는 오버헤드를 조금이라도 줄일 수 있는 소요가 있을 것이다.

### 💻 풀이 코드

```python
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

```

```python
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
```


### 🤔 고찰

- "투포인터 라고 하면 정렬상태" 라는 편견에 갇혀서 문제 풀이에 어려움이 있었던 것 같다. 투포인터의 사용에 있어서 두가지 포인터의 증감 기준만 적절히 설정할 수 있다면 정렬상태가 아니더라도 적용이 가능하다는 사실을 명심해야 할 것이다.
