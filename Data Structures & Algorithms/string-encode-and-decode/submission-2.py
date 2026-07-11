class Solution:

    def encode(self, strs: List[str]) -> str:
        parts=[]
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        print(''.join(parts))
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            parts = []
            while(s[j]!= '#'):
                parts.append(s[j])
                j+=1

            print(parts)
            l = int(''.join(parts))


            ans.append(s[j+1:j+l+1])
            i = j+l+1
        return ans

