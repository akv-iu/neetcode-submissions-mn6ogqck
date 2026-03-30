class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)
        
        while len(self.maxHeap)>1:
            first = heapq.heappop(self.maxHeap)
            print(self.maxHeap)
            second = heapq.heappop(self.maxHeap)
            x = first - second
            print(first,second)
            print(self.maxHeap,x)
            if x < 0:
                heapq.heappush(self.maxHeap, x)
                print(self.maxHeap)
        if len(self.maxHeap) == 0:
            return 0
        return self.maxHeap[0] * -1