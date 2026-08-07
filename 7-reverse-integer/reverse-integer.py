class Solution(object):
    def reverse(self, x):     
        sign = -1 if x<0 else 1
        ans=abs(x)
        rev=str(ans)[::-1]
        revnum= int(rev)*sign 
        if revnum < -2**31 or revnum >2**31-1:
            return 0
        return revnum
    


