class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for s in strs:
            arr = [0] *26
            for c in s:
                arr[ord(c)- ord('a')]+=1
            key = tuple(arr)
            if key not in mp:
                mp[key] = []
            mp[key].append(s)

        return list(mp.values())





