# Class to determine if a string containing '()', '{}', and '[]' has correctly nested and matched pairs using a stack.

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        mapping = {
            ")": "(", 
            "}": "{", 
            "]": "["
            }
        
        for ele in s:
            if ele in mapping:
                top_element = my_stack.pop() if my_stack else "#"
                if mapping[ele] != top_element:
                    return False
            else:
                my_stack.append(ele)
        return not my_stack
