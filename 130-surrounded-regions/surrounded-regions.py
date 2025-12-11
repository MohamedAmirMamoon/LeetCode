class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        newBoard = [row[:] for row in board]
        visited = set()

        def bfs(r, c):
            # find all connected O's, they should either be connected by O's or X, never any no space
            q = deque()
            q.append((r, c))
            visited.add((r, c))



            region = [[r, c]]
            enclosed = True

            directions = [[1,0], [-1,0], [0,1], [0,-1]]            
            
            while q:
                row, col = q.popleft()

                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    enclosed = False

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(rows) and nc in range(cols):
                        if newBoard[nr][nc] == 'O' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            region.append((nr, nc))
                    
            if enclosed:
                for r, c in region:
                    newBoard[r][c] = 'X'
            


        for r in range(rows):
            for c in range(cols):
                if newBoard[r][c] == 'O' and (r, c) not in visited: 
                    bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                board[r][c] = newBoard[r][c]

        