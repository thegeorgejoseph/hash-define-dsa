class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for triplet in triplets:
            if len(res) == 3:
                return True
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    res.add(i)
        return True if len(res) == 3 else False