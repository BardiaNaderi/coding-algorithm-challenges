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
    
# Binary search... somehow slower
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:
#                     return nums[left]
#         middle = right // 2
        
#         for x in nums:
#             if nums[left] <= nums[right]:
#                 return nums[left]
#             if nums[middle] >= nums[left]:
#                 left = middle + 1
#                 middle = left + (right - left) // 2
#             else:
#                 right = middle
#                 middle = left + (middle - left) // 2