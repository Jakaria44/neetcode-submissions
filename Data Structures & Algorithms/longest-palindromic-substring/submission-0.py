class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI , resL = 0,0

        for i in range(len(s)):

            #odd
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:

                if r-l+1 > resL:
                    resI = l
                    resL = r-l+1
                l-=1
                r+=1

            # even
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:

                if r-l+1 > resL:
                    resI = l
                    resL = r-l+1
                l-=1
                r+=1
        return s[resI:resI+resL]