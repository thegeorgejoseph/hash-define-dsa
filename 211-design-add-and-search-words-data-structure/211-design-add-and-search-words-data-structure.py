class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
            self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                char = word[j]
                if char != ".":
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                else:
                    for childNode in curr.children.values():
                        if dfs(j + 1, childNode): return True
                    return False
            return curr.isEnd 
        
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)