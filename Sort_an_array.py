class Solution:
    def sortArray(self, num):
        def merge_sort(a):
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:5])
            return merge(left, right)
        def merge(left, right):
            i = j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return merge_sort(num)
num = list(map(int, input("enter numbers separated by space: ").split()))
obj = Solution()
sorted_nums = obj.sortArray(num)
print("Sorted array:",sorted_nums)
