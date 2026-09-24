class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r - l > 1:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else: # the else case must have nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1