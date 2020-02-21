import numpy as np
import pprint

grid = [
    [7,0,0,0,3,0,0,0,1],
    [0,0,0,1,7,8,0,0,0],
    [0,0,5,0,0,0,2,0,0],
    [0,2,6,0,0,0,4,9,0],
    [0,0,0,0,0,0,0,0,0],
    [0,8,4,0,0,0,7,2,0],
    [0,0,3,0,0,0,6,0,0],
    [0,0,0,3,5,9,0,0,0],
    [4,0,0,0,1,0,0,0,9]]


def solve():
    """
    Arg: matrix 9x9
    Output: solved Sudoku

    """
    global grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if is_possible(i,j,n):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return
                 
            
    
    pprint.pprint(grid)
    input("More?")
    

def is_possible(y,x,n):
    """
    Arg: 
        grid: matrix 9x9
        x: sepecific row
        y: specific column
        n: element(from 1-9)

    Output: solved Sudoku

    """
    global grid
    #rows
    for i in range(9):
        if  grid[y][i] == n:
            return False
    
    #columns
    for i in range(9):
        if grid[i][x] == n:
            return False
    

    #subsquares 3x3
    x1 = (x//3)*3
    y1 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if  grid[i+y1][j+x1] == n:
                return False
    
    #n not founded
    return True

def main():
    """
    Output: simple test with deaufult gird

    """    
    solve()

if __name__ == "__main__":
    main()