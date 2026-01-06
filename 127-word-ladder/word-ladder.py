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

        # we can take advantage of the dict of wordList
        # when in dfs, we take our word, iterate through all letters for each char
        # if that exists in wordList then add it with one extra step
        # 

        q = deque()
        q.append((beginWord, 1))
        wordSet = set(wordList)

        while q:
            word, tMoves = q.popleft()
            if word == endWord:
                return tMoves

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, tMoves+1))
        
            
        return 0
                
            

       