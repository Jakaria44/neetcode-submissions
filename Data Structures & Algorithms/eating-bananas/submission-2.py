class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,u =1, max(piles)
        rate = u
        while u >= l:
            m = int( l + (u-l)/2)

            # hrs = 0
            # for i in piles:
            #     hrs+= math.ceil(i/m)
            hrs = sum(math.ceil(x/m) for x in piles)

            if hrs > h:
                l = m+1
            else:
                u = m-1
                rate = m
        return rate

