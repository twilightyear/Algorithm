

---


# [LeetCode] 35. Search Insert Position


---


### 📌 문제 링크
[LeetCode - Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)


---

### ⚠️ 제약조건
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104



---


### 🛠️ 풀이 접근 및 핵심 로직
- 문제는 정렬된 배열이 주어진 상태에서 순서를 고려하여 인덱스를 찿으면 된다. 여기서 그냥 Bruteforce로 찿아도 O(N)이 나올 것이다. 하지만 정렬되있다는 조건을 활용하여 이분탐색을 사용한다면 시간복잡도를 O(logN)으로 줄일 수 있을 것이다. 여기서는 다만 이분 탐색의 과정에서 target값이 배열에 존재한다면 그 target의 인덱스를 반환하면 그만이지만 없는 상황도 존재한다. 그런 경우에서는 사용 가능한 가장 작은 인덱스인 left를 반환하면 될 것이다.



---


### 📊 복잡도 분석
**시간복잡도**
- 이분탐색을 사용하여 시간복잡도 O(logN)으로 해결 가능하다.

**공간복잡도**
- 이분탐색을 위한 left, right 등의 변수를 위한 별도의 공간이 필요하다. O(1)의 시간복잡도를 가진다.



---


### 📝 회고 / 추후 개선점
- 아주 정석적인 이분 탐색 문제였다. 정렬된 배열이라는 상황에서 적절하게 이분 탐색을 사용했던 것이 적절했다. 기본기를 더 탄탄하게 유지하여 활용이 들어간 문제도 문제없이 접근이 가능해야할 것이다.


---

