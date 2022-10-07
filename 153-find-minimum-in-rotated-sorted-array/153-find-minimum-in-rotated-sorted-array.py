class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, 1
        
        for x in nums:
            if right < len(nums):
                if nums[left] > nums[right]:
                    return nums[right]
                else:
                    left += 1
                    right += 1

        return nums[0]
