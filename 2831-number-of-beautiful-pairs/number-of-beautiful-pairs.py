class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = 0
        n = len(nums)
        
        # Check every pair (i, j) where i < j
        for i in xrange(n):
            first_digit = int(str(nums[i])[0])
            
            for j in xrange(i + 1, n):
                last_digit = nums[j] % 10
                
                # If they are coprime, increment our pair counter
                if gcd(first_digit, last_digit) == 1:
                    ans += 1
                    
        return ans

        