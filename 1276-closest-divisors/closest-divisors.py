class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        start_root = int((num + 2) ** 0.5)      
        for root in range(start_root, 0, -1):
            if (num + 1) % root == 0:
                return [root, (num + 1) // root]
            if (num + 2) % root == 0:
                return [root, (num + 2) // root]
