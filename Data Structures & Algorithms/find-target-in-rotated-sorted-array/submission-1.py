class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
 
        while l < r:
            mid = int(l + (r-l)/2)
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid


        if target == nums[l]:
            return l
        if target <= nums[-1]:
            r = len(nums) - 1
        else:
            l = 0
            r = r -1
        print( l , r, "min")

        while l <= r:
            mid = int(l + (r-l)/2)

            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
