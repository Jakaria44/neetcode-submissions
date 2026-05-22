class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) -1
        maxArea = 0
        while(start<end):
            area = (end-start) * min(heights[start], heights[end])
            maxArea = max(maxArea, area)
            if heights[start] < heights[end]:
                start+=1
            elif heights[start] > heights[end]:
                end-=1
            else:
                start+=1
                end-=1

        return maxArea