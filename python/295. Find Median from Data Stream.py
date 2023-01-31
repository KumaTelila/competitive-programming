class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        l = len(self.data)
        self.data.sort()
        if l%2 == 0:
            a = l//2
            return (self.data[a]+self.data[a-1])/2
        else:
            return self.data[l//2]