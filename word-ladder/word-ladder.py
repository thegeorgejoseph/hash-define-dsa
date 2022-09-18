class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)
        queue = deque([beginWord])
        visit = set([beginWord])
        seq = 1
        while queue:
            for i in range(len(queue)):              
                word = queue.popleft()
                if word == endWord:
                    return seq
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            seq += 1
        
        return 0