#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#Find this single element that appears only once.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        
        return 2*sum(set(nums)) - sum(nums)
