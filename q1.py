def work_life_balance(n, l, h):

    """ 
    Given the length n, l array and h array, you need to compute the maximized revenue V. 
    n: length of both arrays.
    l: easy task revenue array.
    h: difficult task revenue array.
    Return: maximized revenue V.
    """
    
    # create a list for max revenue for n+1 weeks
    max_rev = [0] * (n + 1)
    
    # call max revenue until the i-1th and i-2th week to figure out which to add
    # i-2 for difficult because i-1 will be 0 if week is difficult
    for i in range(n+1):
        
        # set it to 0 so that it doesn't interfere with the sum (week 0)
        if i == 0:
            max_rev[i] = 0
        
        # the first week, set it to be a difficult task 
        elif i == 1:
            max_rev[i] = h[0]
            
        else:
            easy = max_rev[i-1] + l[i-1]
            difficult = max_rev[i-2] + h[i-1]
    
            max_rev[i] = max(easy, difficult)
    
    return max_rev[n]