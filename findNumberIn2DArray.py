class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return False
        else:
            m = len(matrix[0])
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] > target:
                        m = j
                    elif matrix[i][j] == target:
                        return True
            return False