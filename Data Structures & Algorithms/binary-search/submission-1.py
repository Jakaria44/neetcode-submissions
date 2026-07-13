class Solution:

    def bin_search(self, nums, target, start,end) -> int:
        if start> end:
            return -1

        mid = int(start + (end-start)/2)

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.bin_search(nums, target, 0, mid-1)
        else:
            return self.bin_search(nums, target, mid+1,end)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, target, 0, len(nums)-1)

        
