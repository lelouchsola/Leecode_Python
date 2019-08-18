#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        use dictionary to store the difference (target - nums[i]).
        example:
        nums = [2,7,11,15]  target = 9
        1. Initial time diffRec is empty.
        2. num[0] = 2 not in diffRec.keys().
            diff = target - nums[0] = 7, Modify diffRec (empty,{}) into {7:0}
        3. num[1] = 7 is in diffRec, return [diffRec[7], 1]
        """
        diffRec = {}
        for i, v in enumerate(nums):
            if v in diffRec:
                return [diffRec[v], i]
            else:
                diffRec[target - v] = i
        return -1

