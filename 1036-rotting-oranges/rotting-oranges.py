class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        freshOranges = []
        minutes = 0

        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                            
						
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges.append((r,c))
                if grid[r][c] == 2:
                    q.append((r,c,0))

        while q:
            row, col, minItem = q.popleft()
            minutes = max(minutes, minItem)
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr in range(rows) and nc in range(cols):
                    if grid[nr][nc] == 1:
                        q.append((nr, nc, minItem+1))
                        grid[nr][nc] = 2
                            

        for orange in freshOranges:
            r, c = orange
            if grid[r][c] == 1:
                return -1
                                

        return minutes
        # 2 1 1
        # 2 2 0
        # 0 2 2