class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        if n <= 3:
            return []
        if n % 2 != 0:
            target = n - 2
            if target >= 2:
                for i in range(2, int(target**0.5) + 1):
                    if target % i == 0:
                        return []
                return [[2, target]]
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                is_prime[i*i : n+1 : i] = [False] * len(is_prime[i*i : n+1 : i])
                    
        ans = []
        for x in range(2, (n // 2) + 1):
            if is_prime[x] and is_prime[n - x]:
                ans.append([x, n - x])
                
        return ans