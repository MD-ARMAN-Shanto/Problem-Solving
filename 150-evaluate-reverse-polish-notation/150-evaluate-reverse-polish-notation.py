class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        while len(tokens) > 0:
            toke = tokens.pop(0)
            
            if toke not in ['+', '-', '*', '/']:
                stack.append(int(toke))
            else:
                first = stack.pop()
                second = stack.pop()
                if toke == "+":
                    stack.append(second+first)
                elif toke == "-":
                    stack.append(second-first) 
                elif toke == "*":
                    stack.append(second*first)
                elif toke == "/":
                    stack.append(int(float(second)/first))
            # else:
            #     stack.append(int(toke))
        return stack.pop()
                    
        