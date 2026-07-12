class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]
        #                [1,4,1,2,1,0,0]

        stack = []
        ans = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            
            while len(stack) != 0 and temperatures[stack[-1]] < t:
                ind = stack.pop()
                ans[ind] = i - ind
            
            stack.append(i)

        return ans


