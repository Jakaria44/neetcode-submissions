class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1

        maxL,maxR=0,0
        area=0
        while(l<r):
            maxL = max(height[l],maxL)
            maxR = max(height[r], maxR)

            if height[l] >= height[r] :
                r-=1
                area+= max(0, maxR-height[r])
            elif height[l] <height[r]:
                l+=1
                area+= max(0, maxL-height[l])


        return area

