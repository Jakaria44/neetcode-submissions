class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
 
        while l <= r:
            m = int(l + (r-l)/2)
            
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                # left half sorted
                if nums[l] <= target <= nums[m]:
                    # if target is there: continue
                    r = m-1
                else:
                    # move to right half
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1 
        return -1
