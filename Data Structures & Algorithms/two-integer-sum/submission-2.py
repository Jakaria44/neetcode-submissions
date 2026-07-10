class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = {}

        for i,n in enumerate(nums):
            mp[n] = i

        for i,n in enumerate(nums):
            if target-n in mp and mp[target-n] != i:
                return [min(i, mp[target-n]), max(i, mp[target-n])]
            
        return []