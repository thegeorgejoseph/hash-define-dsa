class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        wordList.append(beginWord)
        queue = deque([beginWord])
        seq = 1
        visit = set([beginWord])
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        while queue:    
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return seq
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            seq += 1
        return 0