class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))
            current_area = 0

            while queue:
                r, c = queue.popleft()
                current_area += 1
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = 0

            return current_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        
        return max_area