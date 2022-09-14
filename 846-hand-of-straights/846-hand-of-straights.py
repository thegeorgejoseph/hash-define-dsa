class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freqs = {}
        for num in hand:
            freqs[num] = 1 + freqs.get(num, 0)
        
        minHeap = list(freqs.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            top = minHeap[0]
            for n in range(top, top + groupSize):
                if n not in freqs:
                    return False
                freqs[n] -= 1
                if freqs[n] == 0:
                    if minHeap[0] != n:
                        return False
                    heapq.heappop(minHeap)
        return True