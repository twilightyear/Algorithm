#풀이 1 (Bruteforce)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        for left in range(len(s)):
            count = {}
            for right in range(left, len(s)):
                count[s[right]] = count.get(s[right],0) + 1
                win_length = right - left

                max_count = count[max(count, key=count.get)]

                if(win_length + 1 - max_count <= k):
                    max_length = max(win_length + 1, max_length)
                else:
                    continue

        return max_length
