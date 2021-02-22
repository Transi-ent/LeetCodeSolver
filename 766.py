class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        if not matrix or (matrix and len(matrix[0])==0):
            return False
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    continue
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True

mat = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
]

print(Solution().isToeplitzMatrix(mat))