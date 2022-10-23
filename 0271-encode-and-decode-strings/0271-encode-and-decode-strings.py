# ```
# 3#abc
# i = 0
# j = 1


# ```

class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + "#" + word)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i: j])
            res.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return res
            
        


