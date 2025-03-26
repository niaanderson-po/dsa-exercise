class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        plan:
        first check if 2 input stings are not equal, return false so that in the best case scenerio where the two strings arent equal, then we dont have to go through the rest of the computer loggic
        then create a count is an array that consist of 0s for now
        *finish plan
        """

        if len(s) != len(t):
            return False
        
        count = [0] * 26

        