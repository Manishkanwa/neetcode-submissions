class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_list = set()
        for i in nums:
            if i in in_list:
                return True
            else :
                in_list.add(i)
        return False