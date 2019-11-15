#### 102. Binary Tree Level Order Traversal ####
'''
Given a binary tree, return the level order traversal of its nodes' 
values. (ie, from left to right, level by level).
'''
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		ret = []
		self.dfs(ret,root,0)
		return ret

	def dfs(self,ret,node,level):
		if node == None:
			return False

		if level == len(ret):
			ret.append([])

		ret[level].append(node.val)

		self.dfs(ret,node.left,level+1)
		self.dfs(ret,node.right,level+1)