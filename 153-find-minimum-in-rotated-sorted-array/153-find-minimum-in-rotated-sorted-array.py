class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
                    return nums[left]
        middle = right // 2
        
        for x in nums:
            if nums[left] <= nums[right]:
                return nums[left]
            if nums[middle] >= nums[left]:
                left = middle + 1
                middle = left + (right - left) // 2
            else:
                right = middle
                middle = left + (middle - left) // 2
            