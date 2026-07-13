class TimeMap:
    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp.setdefault(key,[]).append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        
        nums = self.mp[key]
        l, r = 0, len(nums) -1

        ans= ""
        while l <= r:
            mid = (l+r)//2

            if nums[mid][0] <= timestamp:
                l = mid +1
                ans = nums[mid][1]
            else:
                r= mid -1
        return ans

        
