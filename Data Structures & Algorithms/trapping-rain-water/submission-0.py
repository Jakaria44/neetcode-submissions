class Solution:
    def trap(self, height: List[int]) -> int:
        area =0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        currMax =0
        for i,h in enumerate(height):
            currMax = max(currMax,h)
            maxLeft[i] = currMax
        
        currMax =0
        for i,h in enumerate(height[::-1]):
            currMax = max(currMax,h)
            maxRight[len(height) -1 - i] = currMax


        for i, h in enumerate(height):
            minH = min(maxLeft[i], maxRight[i])
            area += max(0, minH-h)

        return area