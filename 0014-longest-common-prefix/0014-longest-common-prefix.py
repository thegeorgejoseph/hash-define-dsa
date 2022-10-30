class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        minWord = strs[0]
        for word in strs:
            if word == "": return ""
            if len(word) < len(minWord): minWord = word
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isEnd = True
        
        curr = root
        query = minWord
        word = ""
        for c in query:
            if len(curr.children) > 1:
                return word
            word += c
            curr = curr.children[c]
        return word