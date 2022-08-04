class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = {}
        for n in hand:
            counts[n] = 1 + counts.get(n,0)
        
        minHeap = list(counts.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            top = minHeap[0]
            for i in range(top, top + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
