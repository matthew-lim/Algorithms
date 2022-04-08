def optimal_path(pyramid):

    """
    Given the pyramid, find the optimal answer and corresponding path for it. 
    pyramid: the number pyramid described in the problem.
    Return: a tuple (answer, path).
    answer is the sum of the optimal route.
    path is the optimal route in the list form.
    """
    n = len(pyramid)
    # copy variable in order so that we don't change the input variable
    # (wasn't aware that we can't change the input before writing the function)
    M = [[0 for j in range(i+1)] for i in range(n)] 
    
    for i in range(n):
        for j in range(i+1):
            M[i][j] = pyramid[i][j]
                        
    # finding the sum of the optimal route
    for i in range(n - 2 , -1, -1):
        for j in range(i+1):
            if M[i+1][j] > M[i+1][j+1]:
                M[i][j] += M[i+1][j]
                
            else:
                M[i][j] += M[i+1][j+1]
    
    pathsum = M[0][0]
    
    # sort out the path it took by looking at the sums
    a = [pathsum]
    index = 0
    for i in range(1,n):
        for j in range(index, index+1):
            
            if M[i][j] > M[i][j+1]:
                a.append(M[i][j])
                
            else:
                a.append(M[i][j+1])
                index = j+1
                
    # subtract by previous values to get its original values
    for i in range(len(a)-1):
        a[i] = a[i] - a[i+1]
                
    return pathsum, a