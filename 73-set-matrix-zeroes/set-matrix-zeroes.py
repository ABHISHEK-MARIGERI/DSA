class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       rows=len(matrix)
       cols=len(matrix[0])

       row_tracker=[0] * rows
       col_tracker=[0] * cols

       for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j]==0:
                row_tracker[i]=-1
                col_tracker[j]=-1

       for i in range(0,rows):
            for j in range(0,cols):
                if row_tracker[i]==-1 or col_tracker[j]==-1:
                    matrix[i][j]=0