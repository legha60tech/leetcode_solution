def combinationSum(candidates, target):
    result = []
    def backtrack(start, path, target):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, target - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result
candidates = list(map(int, input("enter candidates: ").split()))
target = int(input("enter target: "))
result = combinationSum(candidates, target)
print("Combinations are:")
for combo in result:
    print(combo)
            
