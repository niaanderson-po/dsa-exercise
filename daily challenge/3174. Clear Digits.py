#Class to delete the first digit and the closest non-digit character to its left using a stack

class Solution:

    def clearDigits(self, s: str) -> str:
        my_stack = []

        for ele in s:
            if ele.isalpha() == True:
                my_stack.append(ele)
            else:
                if len(my_stack) > 0:
                    my_stack.pop()
        
        return "".join(my_stack)
