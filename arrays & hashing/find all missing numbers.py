#TODO: Check the given list for missing numbers range(1, len(nums))

def findDisappearedNumbers( nums: list[int]) -> list[int]:
        set_nums = set(nums)

        result = []

        for idx in range(1, len(nums) + 1):

            if idx not in set_nums:
                result.append(idx)

        return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1])) 
#Expected Output: [5,6]

print(findDisappearedNumbers([1,1])) 
#Expected Output: [2]
