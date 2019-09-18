"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution(object):
    def most_common_fun(self, A):
        var_count = {}
        var_start = {}
        var_end = {}
        max_common = A[0]
        for idx, item in enumerate(A):
            if item in var_count :
                var_count[item] += 1
                var_end[item] = idx
            else:
                var_count[item] = 1
                var_start[item] = idx
                var_end[item] = idx
            if var_count[item] > var_count[max_common] or (var_count[item] >= var_count[max_common] and (var_end[item] - var_start[item]) < (var_end[max_common] - var_start[max_common])):
                max_common = item
        return max_common


    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        most_common = self.most_common_fun(nums)
        
        return len(nums) - nums[::-1].index(most_common) - nums.index(most_common) 


sol = Solution().findShortestSubArray([1,2,2,3,1,4,2])
print(sol)

sol = Solution().findShortestSubArray([1,2,2,3,1])
print(sol)

sol = Solution().findShortestSubArray([2,1,1,2,1,3,3,3,1,3,1,3,2])
print(sol)
