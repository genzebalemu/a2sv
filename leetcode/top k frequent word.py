class T:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
class Solution(object):
    def topKFrequent(self, words, k):
        ans = []
        heap = []  
        for word, freq in Counter(words).items():
            heapq.heappush(heap, T(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap).word)
        return ans[::-1] 