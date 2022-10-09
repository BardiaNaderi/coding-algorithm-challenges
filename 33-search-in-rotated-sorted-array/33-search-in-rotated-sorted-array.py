class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, (len(nums) - 1)
    
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if nums[left] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:			
                if nums[middle] <= target <= nums[right]:
                    left = middle
                else:				
                    right = middle - 1
                    
        if nums[left] == target:
            return left
        else:
            return -1