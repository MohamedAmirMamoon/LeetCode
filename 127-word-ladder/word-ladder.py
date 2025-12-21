class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        minTransforms = float('inf')
        transformed = False

        edges = []
        words = wordList.copy()
        words.append(beginWord)

        adj = {}
        for word in words:
            adj[word] = []

        for i in range(len(words)):
            for j in range(1+i, len(words)):
                w1 = words[i]
                w2 = words[j]

                countDiff = 0
                for c in range(len(w1)):
                    if w1[c] != w2[c]:
                        countDiff += 1

                if countDiff == 1:
                    adj[w1].append(w2)
                    adj[w2].append(w1)
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth

            for nei in adj[word]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))

        return 0