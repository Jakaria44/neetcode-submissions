class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            mp[n] = 1 + mp.get(n,0)
        

        for key,v in mp.items():
            freq[v].append(key)
         
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num) 
                if len(ans) == k:
                    return ans
            
            
