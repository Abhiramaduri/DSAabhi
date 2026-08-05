class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum=-1
        for i in range(len(arr)-1 ,-1,-1):
            current=arr[i]
            arr[i]=maximum
            if current > maximum:
              maximum=current
        return arr
        