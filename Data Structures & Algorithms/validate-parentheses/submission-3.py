class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        st = []
        for c in s:
            if c in pairs:
                st.append(c)
            elif len(st) > 0 and c == pairs[st[-1]]:
                st.pop()
            else:
                return False

        return len(st) == 0