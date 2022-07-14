class Solution:
#     create test cases before starting to code
# valid case : [], [()]
# invalid case: ][, [), [, ]
    def isValid(self, s: str) -> bool:
        hashmap = {"}": "{", "]" : "[", ")" : "(" } 
        stack = collections.deque()
        
        for par in s:
            if len(stack) == 0 and par in hashmap:
                return False
            
            if par in hashmap:
                top = stack.pop()
                if top != hashmap[par]:
                    return False
            else:
                stack.append(par)
        
        return True if len(stack) == 0 else False