"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

--------------Important---------------------
There are better ways to solve this problem
I'm training comparison loops
--------------------------------------------
"""

nums = [3,2,4]
target = 6

def twoSum(nums, target):

    index_x = 0
    index_j = 0
    if nums[0] + nums[1] == target:
        return [0,1]

    for x in nums:
        index_j = 0

        for j in nums:
            if index_j == index_x:
                index_j += 1
                pass
            elif x + j == target:
                return [index_x, index_j]
            else:
                index_j += 1
        index_x += 1
            
twoSum(nums,target)