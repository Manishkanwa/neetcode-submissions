class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i in range(0,len(nums)):
            remainder = target - nums[i]
            if remainder in new_dict.keys() :
                return  [new_dict[remainder], i]
            else:
                new_dict[nums[i]] = i
        return False
            