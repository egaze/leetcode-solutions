class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0 
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1