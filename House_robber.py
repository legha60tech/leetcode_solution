def rob(nums):
    prev1 = 0
    prev2 = 0
    for num in nums:
        tmp = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = tmp
    return prev1
nums = list(map(int, input("enter house values separated by space: ").split()))
result = rob(nums)
print("Maximum money you can rob:",result)
