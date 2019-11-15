#### 200. Number of Islands #####
'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by water and is 
formed by connecting adjacent lands horizontally or vertically. You
 may assume all four edges of the grid are all surrounded by water.
'''
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if grid == None:
			return false

		count = 0
		# Use DFS to find all ones (island) and set it as visited
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					self.dfs(grid,i,j)
					count = count + 1
		return count

	def dfs(self,grid,i,j):
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
			return
		grid[i][j] = 'VISITED'
		# Recursively get all other ones 
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)