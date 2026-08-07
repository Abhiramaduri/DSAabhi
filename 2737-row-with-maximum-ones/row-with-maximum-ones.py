class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row = 0 
        Max= -1 
        for i in range(len(mat)):
            count = 0 
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count +=1
            if count>Max:
                row = i
                Max=count
        return (row,Max)
            