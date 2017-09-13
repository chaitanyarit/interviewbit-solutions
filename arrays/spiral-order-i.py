class Solution:
    def spiralOrder(self, mat):
        n = len(mat)
        m = len(mat[0])
        r = m
        b = n
        d = 0
        l = 0   
        t = 0
        count = n * m
        result = []
        while count:
            if d == 0:
                for i in range(l, r):
                    result.append(mat[t][i])
                    count -= 1
                d += 1
                t += 1
            elif d == 1:
                for i in range(t, b):
                    result.append(mat[i][r - 1])
                    count -= 1
                r -= 1
                d += 1
            elif d == 2:
                for i in range(l, r):
                    result.append(mat[b - 1][m - i - 2])
                    count -= 1
                b -= 1
                d += 1
            elif d == 3:
                for i in range(t, b):
                    result.append(mat[n - i - 1][l])
                    count -= 1
                l += 1
                d = 0
        return result
