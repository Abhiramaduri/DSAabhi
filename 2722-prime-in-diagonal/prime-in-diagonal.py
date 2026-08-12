class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def is_prime(x):
            if x < 2:
                return False
            # Loop up to the square root of x
            for i in xrange(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        max_prime = 0
        n = len(nums)
        
        for i in xrange(n):
            val1 = nums[i][i]
            if val1 > max_prime and is_prime(val1):
                max_prime = val1
            val2 = nums[i][n - i - 1]
            if val2 > max_prime and is_prime(val2):
                max_prime = val2
                
        return max_prime