def solution(key,lock):
    ksize, lsize = len(key), len(lock)
    answer = False
    board = [ [0 for __ in range(lsize*3)] for _ in range(lsize*3)]
    keys = [key]
    for i in range(3):
        k = [ [0 for __ in range(ksize)] for _ in range(ksize)]
        for ii in range(ksize):
            for iii in range(ksize):
                k[ii][iii] = keys[i][ksize-1-iii][ii] 
        keys.append(k)
            
    for i in range(lsize):
        for ii in range(lsize):
            board[i+lsize][ii+lsize] = lock[i][ii]
    
    for k in range(4):
        for i in range(lsize-ksize,lsize*2):
            for ii in range(lsize-ksize,lsize*2):
                for j in range(ksize):
                    for jj in range(ksize):
                        # print(board[i][ii])
                        # print(keys[k][j][jj])
                        board[i+j][ii+jj] += keys[k][j][jj]

                done = True
                for j in range(lsize,lsize*2):
                    for jj in range(lsize,lsize*2):
                        if board[j][jj] != 1:
                            done = False
                            break
                    if not done:
                        break
                if done:
                    return True

                for j in range(ksize):
                    for jj in range(ksize):
                        board[i+j][ii+jj] -= keys[k][j][jj]

    return answer




# numbers = [[[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]]
numbers = [[[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1,0]]]

print(solution(numbers[0],numbers[1]))

