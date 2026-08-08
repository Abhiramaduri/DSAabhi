class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low,high+1):
            s= str(i)
            if len(s) %2 !=0:
                continue
            mid = len(s)//2
            left_sum=0
            right_sum=0
            for j in range(mid):
                left_sum +=int(s[j])
            for j in range(mid, len(s)):
                right_sum +=int(s[j])

            if left_sum ==right_sum:
                count +=1
        return count   
            