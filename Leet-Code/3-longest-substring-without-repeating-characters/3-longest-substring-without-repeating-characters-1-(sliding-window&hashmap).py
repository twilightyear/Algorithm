#풀이 1 (Sliding Window & Hashmap)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_index = {}

        for right in range(len(s)):
            current_char = s[right]

            if current_char in last_index and last_index[current_char] >= left:
                left = last_index[current_char] + 1

            last_index[current_char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
        
