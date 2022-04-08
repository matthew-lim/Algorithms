def LCS3(X,Y,Z):

    """ 
    Given three strings X, Y, Z, you are to find the longest common subsequence among these three strings.
    X, Y, Z: three input strings as descrbied.
    Return: the length of LCS for these 3 strings.
    """ 
    
    n, m, o = len(X), len(Y) , len(Z)
    M = [[[0 for i in range (o+1)] for j in range(m+1)] for k in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            for k in range(o+1):

                if i == 0 or j == 0 or k == 0:
                    M[i][j][k] = 0

                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    M[i][j][k] = M[i-1][j-1][k-1] + 1
                    
                else:
                    prevX = M[i-1][j][k]
                    prevY = M[i][j-1][k]
                    prevZ = M[i][j][k-1]

                    M[i][j][k] = max(prevX, prevY, prevZ)
    
    return M[n][m][o]

# maybe can reduce the space?