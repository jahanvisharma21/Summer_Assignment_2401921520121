# Reshape the matrix
class Solution:
    def matrixReshape(self, mat, r, c):
        flat = [num for row in mat for num in row]
        
        if len(flat) != r * c:
            return mat
        
        res = []
        for i in range(0, len(flat), c):
            res.append(flat[i:i+c])
        
        return res       