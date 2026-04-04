def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = []
    for start, end in intervals:
        if not res or res[-1][1] < start:
            res.append([start, end])
        else:
            res[-1][1] = max(res[-1][1], end)
    return res
n = int(input("enter number odf intervals: "))
intervals = []
for i in range(n):
    start, end = map(int, input(f"Enter interval {i+1} (start end): ").split())
    intervals.append([start, end])
result = merge(intervals)
print("merged intervals:", result)
