class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            #the first s1 characters of s2 have been mapped too so start loop from s1 to s2
            count2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if count1[i]==count2[i] else 0)
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[right]) - ord('a')
            count2[index] += 1
            if count2[index] == count1[index]:
                matches += 1
                # well technically the count2[index] could have kept on increasing so we need to see if its a 0 and 1 match herer
            elif count1[index] + 1 == count2[index]:
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            left += 1
        return matches == 26
            
