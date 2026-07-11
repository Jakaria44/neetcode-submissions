class Solution:

    def encode(self, strs: List[str]) -> str:
        parts=[]
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s) 
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            parts = []
            while(s[j]!= '#'): 
                j+=1
 
            l = int(s[i:j])

            ans.append(s[j+1 : j+l+1])
            i = j + l + 1
        return ans

