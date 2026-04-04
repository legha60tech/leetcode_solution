import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  
        self.large = []
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0
medianFinder = MedianFinder()
print("Enter numbers one by one. Type 'q' to quit.\n")
while True:
    x = input("Enter number: ").strip()
    if x.lower() == 'q':
        print("Exiting...")
        break
    try:
        num = int(x)
        medianFinder.addNum(num)
        print(f"Added {num}, current median: {medianFinder.findMedian()}")
    except ValueError:
        print("Invalid input! Enter a number or 'q' to quit.")
