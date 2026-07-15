class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub = nums[0]
        # currSum = 0
        # for n in nums:
        #     if currSum < 0:
        #         currSum = 0
        #     currSum+= n
        #     maxSub = max(maxSub, currSum)
        # return maxSub

        dp = nums[:]
        # dp[i] = max subarray sum  ending at i
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        # for i, n in enumerate(nums[1:]):
        #     dp[i] = max(n, n+dp[i-1])
        return max(dp)