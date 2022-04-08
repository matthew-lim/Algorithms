def max_average(n, H, g, f_list):

    """
    Given the functions and grade scale, find the optimal average grade a student can get according to the problem description.
    n: number of functions H: total amount of hour.
    g: grade scale.
    f_list: a list of functions Return: maximum average grade one can get. 
    """
    
    M = [[0 for j in range(H+1)] for i in range(n+1)]
 
    def score(n, h):
        if h == 0:
            return 0
        elif f_list[n-1](h) > g:
            return g
        else:
            return f_list[n-1](h)
    
    for i in range(1, n+1):
        for j in range(H+1):
            for k in range(j+1):
                if score(i, k) + M[i-1][j-k] > M[i][j]:
                    M[i][j] = score(i,k) + M[i-1][j-k]

                
    return M[n][H]/n