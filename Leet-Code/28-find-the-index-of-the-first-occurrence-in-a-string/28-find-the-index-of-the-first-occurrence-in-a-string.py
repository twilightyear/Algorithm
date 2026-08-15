class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if(haystack==needle):
            return 0

        needle_length = len(needle)
        for i in range(0,len(haystack)-needle_length+1):
            if haystack[i:i+needle_length] == needle:
                return i


        return -1
