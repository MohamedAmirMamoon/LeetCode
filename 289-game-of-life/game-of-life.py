class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [[1,-1],[1, 1], [-1, 1], [-1, -1], [0,1], [0, -1], [1, 0], [-1, 0]]
	
        def checkBFS(r,c):
            liveCounter = 0
            currentItem = board[r][c]	
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if nr in range(rows) and nc in range(cols):
                    if board[nr][nc] == 1 or board[nr][nc] == 2:
                        liveCounter += 1	
            if currentItem == 1 or currentItem == 2:
                    # the checks for live if needs to change, make it 2
            # otherwise we keep it the same
                if liveCounter < 2 or liveCounter > 3:
                    board[r][c] = 2
            else:
                # the checks for live if needs to change, make it 3
            # otherwise we keep it the same
                if liveCounter == 3:
                    board[r][c] = 3
                        
                    

        for r in range(rows):
            for c in range(cols):
                checkBFS(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                if board[r][c] == 3:
                    board[r][c] = 1
