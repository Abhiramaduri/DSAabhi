import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        
     
        p //= g
        q //= g
        
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1

        