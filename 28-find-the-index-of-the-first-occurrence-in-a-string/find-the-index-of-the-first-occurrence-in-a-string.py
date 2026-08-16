class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
            
        h_len = len(haystack)
        n_len = len(needle)
        
        for i in xrange(h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
                
        return -1