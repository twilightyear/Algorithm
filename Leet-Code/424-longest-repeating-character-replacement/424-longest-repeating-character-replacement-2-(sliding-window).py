#풀이 2 (Sliding Window)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = {}

        for right in range(left, len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            win_length = right - left

            max_count = count[max(count, key=count.get)]

            if(win_length + 1 - max_count <= k):
                max_length = max(win_length + 1, max_length)
            else:
                count[s[left]] -= 1
                left += 1

        return max_length
