from collections import Counter
class Solution:
    def MinWindow(self, a, b):
        if not a or not b:
            return ""
        b_count = Counter(b)
        window = {}
        have, need = 0, len(b_count)
        res = [-1, -1]
        res_len = float("inf")
        left = 0
        for right in range(len(a)):
            char = a[right]
            window[char] = window.get(char, 0)+ 1
            if char in b_count and window[char] == b_count[char]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left,right]
                    res_len = right - left + 1
                window[a[left]] -= 1
                if a[left] in b_count and window[a[left]] < b_count[a[left]]:
                    have -= 1
                left += 1
        l,r = res
        return a[l:r+1] if res_len != float("inf") else ""
a = input("Enter the string a :")
b = input("Enter the string b :")
obj = Solution()
result = obj.MinWindow(a,b)
print("output:", result)
