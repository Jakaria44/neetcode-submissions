class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        right = [1] * len(nums)

        left[1] = nums[0]
        right[len(nums)-2] = nums[len(nums)-1]
        
        for i in range(2, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        print(left)
        
        for i in range(len(nums) -3, -1, -1):
            right[i] = right[i+1]* nums[i+1]

        print(right)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]
        return ans