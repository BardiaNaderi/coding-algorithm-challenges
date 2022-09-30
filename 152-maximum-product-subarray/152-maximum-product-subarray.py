class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for x in nums:
            if x == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * x
            temp2 = x * curMin
            curMax = max(temp, temp2, x)
            curMin = min(temp, temp2, x)
            res = max(res, curMax)
            
        return res