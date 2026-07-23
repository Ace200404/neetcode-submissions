class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token in ['+','-','/','*']:
                sec_val=stack.pop()
                fir_val=stack.pop()

                if token=='+':
                    stack.append(fir_val+sec_val)
                elif token=='-':
                    stack.append(fir_val-sec_val)
                elif token=='/':
                    stack.append(int(fir_val/sec_val))
                else:
                    stack.append(fir_val*sec_val)
            else:
                stack.append(int(token))
        return stack[0]
