from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()

nums = [3,4,5,6]
target = 7

print (sol.twoSum(nums, target))

nums = [4,5,6]
target = 10

print (sol.twoSum(nums, target))

nums = [5,5]
target = 10

print (sol.twoSum(nums, target))
