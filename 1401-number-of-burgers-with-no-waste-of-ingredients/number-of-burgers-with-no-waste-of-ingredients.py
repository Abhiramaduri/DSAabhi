class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices % 2 != 0:
            return []

        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo

        if jumbo < 0 or small < 0:
            return []

        return [jumbo, small]