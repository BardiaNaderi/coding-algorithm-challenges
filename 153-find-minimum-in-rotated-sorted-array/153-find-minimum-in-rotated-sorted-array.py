class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallestVal = nums[0]
        left, right = 0, 1
        for x in nums:
            if right < len(nums):
                if nums[left] > nums[right]:
                    smallestVal = nums[right]
                else:
                    left += 1
                    right += 1
        return smallestVal