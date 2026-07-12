class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = [1] * n

        for i in range(1, n):
            ans[i] = nums[i-1] * ans[i-1]
        
        print(ans)
        temp = 1
        for i in range(n -2, -1, -1):
            temp *= nums[i+1]
            ans[i] *= temp

 

        return ans