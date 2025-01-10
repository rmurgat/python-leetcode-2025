import math
from typing import List


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
                 