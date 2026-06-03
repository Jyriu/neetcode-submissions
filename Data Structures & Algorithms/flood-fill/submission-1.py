class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # find the image[sr][sc] pixel -> starting point
        # change its color to color
        # do same thing for its ajdacents pixels that share the same color recursively for all pixel

        if image[sr][sc] == color:
            return image

        def dfs(image, sr, sc, color, original_color):
            ROWS, COL = len(image), len(image[0])
            if min(sr, sc) < 0 or sr == ROWS or sc == COL or image[sr][sc] != original_color:
                return
            
            image[sr][sc] = color

            dfs(image, sr + 1, sc, color, original_color)
            dfs(image, sr - 1, sc, color, original_color)
            dfs(image, sr, sc + 1, color, original_color)
            dfs(image, sr, sc - 1, color, original_color)

            return
        
        dfs(image, sr, sc, color, image[sr][sc])

        return image