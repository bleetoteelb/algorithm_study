def solution(N, number):
    d = N
    cases = [set() for i in range(8)]
    cases[0].add(d)
    if N == number:
        return 1
    
    for i in range(1,8):
        d = d*10 + N
        cases[i].add(d)
        
        for ii in range(i):
            for x in cases[ii]:
                for y in cases[i-ii-1]:
                    cases[i].add(x+y)
                    cases[i].add(x-y)
                    cases[i].add(x*y)
                    
                    if not y ==0: cases[i].add(x//y)
                    
        if number in cases[i]:
            return i+1
    else:
        return -1
