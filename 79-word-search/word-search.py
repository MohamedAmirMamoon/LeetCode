class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        wordExists = False
        visited = set()
        def dfs(r, c, wordIndex):
            nonlocal wordExists
            if wordExists or (r,c) in visited: 
                return 
            if not (r in range(rows) and c in range(cols)):
                return 
            if board[r][c] != word[wordIndex]:
                return 
            if wordIndex == len(word) - 1:
                wordExists = True
                return

            visited.add((r, c))
            dfs(r+1, c, wordIndex+1)
            dfs(r-1, c, wordIndex+1)
            dfs(r, c+1, wordIndex+1)
            dfs(r, c-1, wordIndex+1)
            visited.remove((r, c))
            
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r, c, 0)

        if wordExists: 
            return True
        
        return False