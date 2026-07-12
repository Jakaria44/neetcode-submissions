class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls = []

        for t in tokens:
            if t == '+':
                ls[-2] += ls[-1]
                ls.pop()
            elif t == '-':
                ls[-2] -= ls[-1]
                ls.pop()
            elif t == '*':
                ls[-2] *= ls[-1]
                ls.pop()
            elif t == '/':
                ls[-2] = int(ls[-2]/ls[-1])
                ls.pop()
            else:
                ls.append(int(t))
            print(ls)
            
        return ls[0]

            
            