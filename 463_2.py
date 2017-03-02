class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        res=0

        for i in grid:
            res+=sum(i)
        res=res*4
        i=0
        
        while i<m:
            j=0
            while j<n:
                if j<n-1 and grid[i][j] ==1 and grid[i][j+1]==1 :
                    res=res-2
                j=j+1
            i=i+1
        i=0
        j=0
        while i<n:
            j=0
            while j<m:
                if j<m-1 and grid[j][i] ==1 and grid[j+1][i]==1 :
                    res=res-2
                j=j+1
            i=i+1
        return res      
        
