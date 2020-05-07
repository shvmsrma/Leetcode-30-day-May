#Given an array of size n, find the majority element.
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        maxv = 0
        for k,v in freq.items():           
            if(v> len(nums)/2):
                return k
