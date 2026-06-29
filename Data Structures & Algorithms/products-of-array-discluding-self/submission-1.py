class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        final = [0] * len(nums)
        for i in range(0,len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j] == 0:
                        return [0]* len(nums)
                    else:
                        product *= nums[j]
                final[i] = product
                return final 
                break
            else :
                product *= nums[i]
        for i,num in enumerate(nums):
            final[i] = int(product/num)

        return final