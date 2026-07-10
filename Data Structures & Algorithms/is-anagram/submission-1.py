class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False

        """
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] +=1

        
        for c in t:
            count[ord(c) - ord('a')] -=1

        return all(x == 0 for x in count)
        """

        cntS, cntT = {}, {}

        for i in range(len(s)):
            cntS[s[i]] = 1 + cntS.get(s[i], 0)
            cntT[t[i]] = 1 + cntT.get(t[i], 0)

        return cntS == cntT
