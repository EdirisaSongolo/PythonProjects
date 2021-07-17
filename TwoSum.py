
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in nums:
                remainder_index = nums.index(remainder)
                sol_list = [index, remainder_index]
        return sol_list
