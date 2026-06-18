class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0



        st = set() 
        length =0
        while j < len(s): 
            while s[j] in st:
                
                st.remove(s[i])
                i+=1
            st.add(s[j]);
            length = max(length, j-i+1)
            j+=1
        return length



        