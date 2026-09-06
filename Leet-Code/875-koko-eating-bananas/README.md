### [ LeetCode ] 875. Koko Eating Bananas

### 📌 문제 링크

[LeetCode - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

### ⚠️ 제약조건

- 1 <= piles.length <= 104
- piles.length <= h <= 109
- 1 <= piles[i] <= 109

### 🛠️ 풀이 접근 및 분석

> Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

> Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

> Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

> Return the minimum integer k such that she can eat all the bananas within h hours.

-   **접근 1**
  - 문제에서는 시간 h 내에 적절한 k 값을 구하는 것을 목적으로 하고 있다. Koko 는 한시간에 k 개의 바나나를 먹을 수 있을때, piles의 첫 인덱스 에서 만약 2k+1 의 바나나가 주어졌다고 하면 3 시간이 걸리는 것 처럼, ceil() 를 이용한 오름차순 계산을 통하여 계산을 해 줄 필요가 있다.
  - 문제를 풀기 위해서, Bruteforce 를 사용하여 풀이를 해주었다. 결국 음식을 먹기 위한 k 의 범위는 1 부터 max(piles) 값임을 알 수 있는데, 이를 이용한 for 문의 구성으로, 모든 k 에 대한 먹는 시간을 구해줄 수 있다. 이때 주어진 h 와 처음 같아질때 h 를 반환하는 코드를 구성했다. 하지만 시간초과가 발생하여 다른 접근 방식을 생각해줄 필요가 있었다. 이 방식으로는 모든 경우에서도 공간복잡도는 O(1) 을 가지지만, 배열의 길이 L, 배열의 최대값 N 에 대하여, 최악의 경우 O(L*N)의 시간복잡도를 가진다.
-   **접근 2**
  - Bruteforce 에서 사용한 방식에서 아주 조금 변환만 해주면 문제를 해결해 줄 수 있다. k 의 값을 1부터 max(piles) 까지의 범위에서 찿아준다는 핵심 내용을 이용하여, k 값에 대한 Binary Search 를 사용한다. 이때 Binary Search 를 사용하여 알아낸 k 값을, 그대로 for 문을 사용하여, 소요되는 시간을 구해주고, 이 시간이 h 보다 크다면 너무 한번에 적게 먹는다는 의미이니, left = mid + 1, 반대로 h 보다 작다면, right = mid - 1 를 통하여 범위를 좁히며, 같아질 경우에 mid 값을 반환하여 적절한 k 값을 알아내는 방식을 생각해냈다. 하지만 테스트 케이스를 돌리니 일부 케이스에서 틀린 답을 내놓아, 다른 방식의 탐색이 필요했다.

- 아래 코드가 문제가 있었던 부분이다. 문제는 조건을 만족하는 가장 작은 k 를 찿는게 핵심이다. 그렇기에 hours == h 를 만족하더라도, 더 작은 값을 찿을 수 있어야하지만, 아래 코드를 통해서는 hours == h 를 만족하는 처음 만난 k 값을 바로 반환하기에 일부 테스트 케이스에서는 틀린 답이 반환된 것이다.
```python
if hours < h: 
  right = mid - 1
elif hours > h:
  left = mid + 1
else:
  return mid
```
- 그렇기에 아래 코드처럼, 정답을 반환하는 로직은 루프가 끝난 후 반환되도록, 따로 while 문 밖으로 빼버리고, hours <= h 인 경우에 대하여 최대한 right = mid - 1 를 통하여 조건에 맞는 영역에서 mid 값을 최소화 하는 방식으로 코드를 수정할 필요가 있었다. 이렇게 접근 1번의 방식은 O(L*N) 의 시간복잡도를 가지는데, 접근 2번에서는 모든 경우에서도 공간복잡도는 O(1) 을 가지지면서도, O(LlogN) 시간복잡도를 가지도록 바꿀 수 있었다.

```python
if hours <= h:
  ans = mid
  right = mid - 1
else:
  left = mid + 1
```
- 이를 통하여 정상적인 코드 제출이 가능했다.

### 📝 추후 개선점

- Bruteforce 에서 Binary Search 로의 논리 확장의 사고과정은 좋았다고 생각하지만, 결국 저번 문제처럼 세부적인 로직 구현에서 조그마한 요소 때문에 문제를 결국 틀리게 되었던 경우가 되었다. 결국 이러한 예외 처리를 포함한 로직의 디테일이 알고리즘 코딩 테스트의 실력을 좌지우지한다고 생각하기에, 로직 구현에서 더 발전이 있어야할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (Bruteforce)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(1,max(piles)+1): #가능한 k 값 전부 조회

            hours = 0
            for i in range(len(piles)): #k 값에 대한 걸리는 시간 확인
                hours += math.ceil(piles[i]/k)
            
            if(hours == h):
                return k
```

```python
#풀이 1 (Binary Search)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while(left<=right):

            mid = left + (right - left) // 2 #K 값에 대한 Binary Search

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            
            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return ans
```

### 🤔 고찰

- 생각보다 문제 이해가 직관적으로 다가오지 않았던 문제이다. 하지만 상당히 재미있게 풀었던 문제였다고 생각한다. 막연하게 Bruteforce 로 풀었던 풀이 방식에서 Binary Search 로 확장해서 시간복잡도 개선이 가능할 것이라고 생각하여 바꾸면서 왠지 모를 희열감이 있었던 것 같다. 앞으로도 꾸준히 정진하여 기본 실력을 늘려나가자.
