class Solution:
    def rotate(self,matrix):
        length=len(matrix)

        for row in range(len(matrix)):
            for column in range(row+1,len(matrix)):
                temp=matrix[row][column]
                matrix[row][column]=matrix[column][row]
                matrix[column][row]=temp

        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        return matrix



s=Solution()
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(s.rotate(matrix))