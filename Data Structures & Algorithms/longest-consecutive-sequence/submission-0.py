class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        st = set()

        for i in nums:
            st.add(i)

        starts = []
        for n in nums:
            if n-1 not in st:
                starts.append(n)

        ans = 0
        cnt = 0
        for i in starts:
            j = i
            while j in st:
                cnt+=1  
                j+=1
                print(cnt)
            ans = max(ans,cnt)
            cnt = 0

        return ans  
            