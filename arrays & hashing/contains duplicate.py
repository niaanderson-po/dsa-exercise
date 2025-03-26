#Return true is an interger array nums contains duplicate values, false otherwise

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        #input lst[int] 
        #output bool

        """
        Understand clarification: would you like for me to prioritize time or space complexity?

        plan:
        use set for unique values and compare to len of input
        *reason is we only need to return a bool, not any specific information that may require more steps like returning the minimum index where a duplicate occured

        time complexity: o(n) because creating a set requires search in array o(n)
        space complexity: o(n) because I set(nums) require additional memory proportional to n unique elements
        """

        unique = set(nums)
        return len(unique) != len(nums)
    
        #or 

        return len(set(nums)) < len(nums)