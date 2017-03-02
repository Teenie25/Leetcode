class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        sum=0
        i=0
        if n>1 and m>1:
            while i<n:
                j=0
                while j<m:
                    if grid[i][j]==1:
                        if (i==0) and (j>0) and (j<m-1):
                            sum=sum+4-grid[i][j-1]-grid[i][j+1]-grid[i+1][j]
                        if (j==0) and (i>0) and (i<n-1):
                            sum=sum+4-grid[i-1][j]-grid[i+1][j]-grid[i][j+1]
                        if (i==n-1) and (j<m-1) and (j>0):
                            sum=sum+4-grid[i][j-1]-grid[i][j+1]-grid[i-1][j]
                        if (j==m-1) and (i<n-1) and (i>0):
                            sum=sum+4-grid[i-1][j]-grid[i+1][j]-grid[i][j-1]
                        if (i==0) and (j==0):
                            sum=sum+4-grid[i+1][j]-grid[i][j+1]
                        if (i==n-1) and (j==0):
                            sum=sum+4-grid[i-1][j]-grid[i][j+1]
                        if (i==n-1) and (j==m-1):
                            sum=sum+4-grid[i-1][j]-grid[i][j-1]
                        if (i==0) and (j==m-1):
                            sum=sum+4-grid[i][j-1]-grid[i+1][j]
                        elif (i>0) and (i<n-1) and (j<m-1) and (j>0):
                            sum=sum+4-grid[i-1][j]-grid[i][j-1]-grid[i+1][j]-grid[i][j+1]
                    else:
                        sum=sum
                    j=j+1
                i=i+1
        if n==1 and m>1:
            j=0
            while j<m:
                if grid[i][j]==1:
                    if (j>0) and (j<m-1):
                        sum=sum+4-grid[i][j-1]-grid[i][j+1]
                    if (j==0):
                        sum=sum+4-grid[i][j+1]
                    if (j==m-1):
                        sum=sum+4-grid[i][j-1]
                    else:
                        sum=sum
                j=j+1
                    
        if m==1 and n>1:
            j=0
            while i<n:
                if grid[i][j]==1:
                    if (i>0) and (i<n-1):
                        sum=sum+4-grid[i-1][j]-grid[i+1][j]
                    if (i==0):
                        sum=sum+4-grid[i+1][j]
                    if (i==n-1):
                        sum=sum+4-grid[i-1][j]
                i=i+1
        if n==1 and m==1:
            if grid[0][0]==1:
                sum=4
            else: 
                sum=0
        return sum
                
        
