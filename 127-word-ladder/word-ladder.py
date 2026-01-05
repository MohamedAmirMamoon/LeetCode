class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # begin word to end word
        # wordList arr is a sequence of words
        # every adjacent pair of words differs by single char
        # so begin word not in wordlist

        # number of words, shortest transform sequence from begin ot end or 0 if none exist
        # this is shortest path
        # do bfs

        # create adj list
        # if word only has exactly one differing char, then we add to its adj list
        # having an adj list we can run bfs
        # call bfs(beginWord), when we reach endWord first time we return and its depth
        # 
        if endWord not in wordList:
            return 0

        # we create adj
        # why do we need adjc
        # iterate through neibors in adj
        # append to queue
        # hit hot
        # 
        
        wordList.append(beginWord)
        adj = {}
        for word in wordList:
            adj[word] = []
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                word = wordList[i]
                wordtwo = wordList[j]
                numDiff = 0
                if word == wordtwo:
                    continue
                for t in range(len(word)):
                    if word[t] != wordtwo[t]:
                        numDiff += 1
                # now if only one char diff add to adj
                if numDiff == 1:
                    adj[word].append(wordtwo)
                    adj[wordtwo].append(word)

        # now we do bfs
        # we give input beginWord, and it checks each nei adding depth and then we return depth if we get to end word

        q = deque()
        q.append((beginWord, 1))
        visited = set(beginWord)

        while q:
            # now we check their adj neighbors
            word, tMoves = q.popleft()
            if word == endWord:
                return tMoves

            
            for nei in adj[word]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, tMoves+1))
            
        return 0
                
            

       