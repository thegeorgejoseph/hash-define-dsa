class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}
        
        for c1, c2 in zip(s,t):
            if (c1 in st and st[c1] != c2 ) or (c2 in ts and ts[c2] != c1):
                return False
            st[c1] = c2
            ts[c2] = c1
        return True