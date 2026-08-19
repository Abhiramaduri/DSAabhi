class Solution(object):
    def findColumnWidth(self, grid):
        """:type grid: List[List[int]]

        :rtype: List[int]
        """
        return [max(len(str(num)) for num in col) for col in zip(*grid)]
        