class solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(num[i],current_sum+ nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
nums = list(map(int, input("enter numbers: ").split()))
obj = solution()
result = obj.maxSubArray(nums)
print("Maximum Subarray Sum:", result)
            
