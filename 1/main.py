from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums[index + 1:]):
                if value + value2 == target:
                    return [index, index + index2 + 1]

    @staticmethod
    def two_dict(nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i


if __name__ == '__main__':
    print(Solution.twoSum([2, 7, 11, 15], 9))
