import math
import numpy as np
from typing import Counter, List


class MatrixBundle01:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(1, len(matrix)):
            left, right = 0, len(matrix[i-1])-1
            while left <= right:
                mid = math.floor((right-left)/2)+left
                if matrix[i-1][mid]<target:
                    left = mid + 1
                elif matrix[i-1][mid]>target:
                    right = mid -1
                else:
                    return True
        return False
                 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = np.array(board)
        L = len(board)
        pos = [0, 3, 6]
        #funtion to find duplicates
        def hasduplicates(a) -> bool:
            d = {}
            for row in a:
                for x in row:
                    if x!=".":
                        n = d.get(x,0)
                        if n==1: return True
                        d[x]= n + 1
            return False
        #validate each row
        for i in range (0, L):
            row = a[i]
            if hasduplicates(row): return False
        #validate each column
        for i in range (0, L):
            col = [row[i] for row in a]
            if hasduplicates(col): return False
        #validate each square
        for i in pos:
            for j in pos:
                square = a[i:i+3,j:j+3]
                if hasduplicates(square): return False
        return True