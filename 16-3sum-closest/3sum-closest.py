class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(ans - target):
                    ans = current_sum
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans

        