class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u = max(piles)
        l = 1

        rate = u
        while u >= l:
            m = int( l + (u-l)/2)

            hrs = 0
            for i in piles:
                hrs+= math.ceil(i/m)

            if hrs > h:
                l = m+1
            else:
                u = m-1
                rate = m
        return rate

