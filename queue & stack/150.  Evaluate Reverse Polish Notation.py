#Class to evaluate an arithmetic expression in Reverse Polish Notation and return the resulting integer

class Solution:
    
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue
          
            right = stack.pop()
            left = stack.pop()
                
            res = 0
            if token == "+":
                res = left + right
            elif token == "-":
                res = left - right
            elif token == "*":
                res = left * right
            elif token == "/":
                res = int(left / right)
 
            stack.append(res)
        
        return stack.pop()