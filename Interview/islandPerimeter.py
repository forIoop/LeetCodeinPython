class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        #Step 1 Search through out grid for 1's
        
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += countPerimeter(grid, i, j)
                    #Now we have to count perimeter at this position
        return perimeter           
                
        
    def countPerimter(grid, i, j):
        count = 0
        #Where water is on left
        if j - 1 < 0 or grid[i][j-1] == 0:
            count += 1
            
        #Where water is on the right
        if j + 1 >= grid[0].length or grid[i][j + 1] == 0:
            count += 1
        
        #Where water is up 
        if i - 1 < 0 or grid[i-1][j] == 0:
            count += 1
            
        #Where water is down
        if i+ 1 >= grid[0].length or grid[i + 1][j] == 0:
            count += 1
            
        return count
