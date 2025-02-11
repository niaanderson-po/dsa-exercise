#Class to count the total number of bad pairs (if i < j and j - i != nums[j] - nums[i]) in an array by using a hash map

from collections import defaultdict

class Solution:
    
    def countBadPairs(self, nums: list[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            total_pairs += i
            good_pairs += count[nums[i] - i]
            count[nums[i]-i] += 1
        return total_pairs - good_pairs