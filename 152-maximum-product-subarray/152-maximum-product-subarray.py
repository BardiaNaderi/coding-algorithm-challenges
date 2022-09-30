class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for x in nums:
            if x == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * x
            curMax = max(temp, x * curMin, x)
            curMin = min(temp, curMin * x, x)
            res = max(res, curMax)
            
        return res