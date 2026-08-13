class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n):
            running_lcm = nums[i]
            for j in range(i, n):
                running_lcm = (running_lcm * nums[j]) // math.gcd(running_lcm, nums[j])
                
                if k % running_lcm != 0:
                    break
                    
                if running_lcm == k:
                    ans += 1
                    
        return ans