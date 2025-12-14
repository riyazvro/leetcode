class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(matrix)
        m=len(matrix[0])
        if m==n:
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            return matrix
        else:
            revmat=[[0 for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    revmat[i][j]=matrix[j][i]
            return revmat
        