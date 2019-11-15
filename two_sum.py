### TWO SUM PROBLEM ####
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	# Using hash tables for low time complexity 
    	table = {}
    	for i in range(len(nums)):
    		table[nums[i]] = i

    	for i in range(len(nums)):
    		if target - nums[i] in table:
    			if table[target-nums[i]] != i:
    				return i, table[target-nums[i]]