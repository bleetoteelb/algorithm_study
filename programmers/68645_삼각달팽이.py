def solution(n):
    answer = []
    idx = 1
    
    tri = [[0 for j in range(i)] for i in range(1,n+1)]
    
    dir = 1 # 1 is down / 2 is right / 3 is up-left
    step = n
    i = -1
    j = 0 
    # make triangle
    while(step > 0):
        if dir == 1:
            for s in range(1,step+1):
                tri[i+s][j] = idx
                idx += 1
            i += step
            dir = 2
            step -= 1
        elif dir == 2:
            for s in range(1,step+1):
                tri[i][j+s] = idx
                idx += 1
            j += step
            dir = 3
            step -= 1
        else:
            for s in range(1,step+1):
                tri[i-s][j-s] = idx
                idx += 1
            i -= step
            j -= step
            dir = 1
            step -= 1
        
    return sum(tri,[])
