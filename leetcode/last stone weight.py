class Solution(object):
    def lastStoneWeight(self, stones):
        for stone in stones:
            heap=[]
            heapq.heappush(heap,-stone)
        while len(heap)>=2:
            x1 = heapq.heappop(heap)
            x2 = heapq.heappop(heap)
            if x1 != x2:
                heapq.heappush(heap,(x1-x2))
        return -heap[-1] if heap else 0