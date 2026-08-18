class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == n:
            return max(nums)
        
        cnt = Counter(nums)
        
        if k == 1:
            res = -1
            for num in cnt:
                if cnt[num] == 1:
                    res = max(res, num)
            return res
        
        res = -1
        if cnt[nums[0]] == 1:
            res = max(res, nums[0])
        if cnt[nums[-1]] == 1:
            res = max(res, nums[-1])
        return res
        