class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in char_set:
                left = max(left, char_set[s[right]] + 1)
            char_set[s[right]] = right
            max_length = max(max_length,right - left + 1)
        return max_length
s = input("enter string: ")
obj = Solution()
print("output:", obj.lengthOfLongestSubstring(s))
