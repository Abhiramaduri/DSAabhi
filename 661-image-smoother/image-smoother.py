class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        
        # Phase 1: Calculate averages and encode into higher bits
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                for i in range(max(0, r - 1), min(m, r + 2)):
                    for j in range(max(0, c - 1), min(n, c + 2)):
                        total_sum += img[i][j] & 255
                        count += 1
                avg = total_sum // count
                img[r][c] |= (avg << 8)
        for r in range(m):
            for c in range(n):
                img[r][c] >>= 8
                
        return img
