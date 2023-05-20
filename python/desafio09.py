def numCells(grid):

        grid_rows = int(input().strip())
        grid_columns = int(input().strip())

        grid = [[1,2,7],[4,5,6],[8,8,9]]

        for _ in range(grid_rows):
            grid.append(list(map(int, input().rstrip().split())))

        result = numCells(grid)

a = 0
numCells(a)        
