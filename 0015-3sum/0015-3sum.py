class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        nums.sort()
        
        for i, x in enumerate(nums):
            if (i > 0 and x == nums[i - 1]):
                continue
            l, r = i + 1, (len(nums) - 1)
            
            while (l < r):
                sum = nums[l] + nums[r] + x
                if (sum > 0):
                    r = r - 1
                elif (sum < 0):
                    l = l + 1
                else:
                    finalList.append([nums[l], nums[r], x])
                    l = l + 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l = l + 1
        return finalList
