def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
nums = list(map(int, input("enter elements sepaarted by space: ").split()))
result = subsets(nums)
print("all subsets are:")
for subset in result:
    print(subset)
