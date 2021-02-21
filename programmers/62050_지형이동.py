import queue
def solution(land, height):
    answer = 0
    lsize = len(land)
    for i in range(lsize):
        for j in range(lsize):
            land[i][j] = [land[i][j],-1]
    def isIn(i,j):
        if i<0 or i>=lsize or j<0 or j>=lsize:
            return False 
        else:
            return True 
    # 4 dir
    dirs = [[-1,0],[0,-1],[1,0],[0,1]]
    # grouping
    gcnt = 0
    q = queue.Queue()
    for i in range(lsize):
        for j in range(lsize):
            if land[i][j][1]>0:
                continue
            print ("start ",i, j)
            gcnt += 1
            q.put([i,j])
            land[i][j][1] = gcnt
            while(not q.empty()):
                tmp = q.get()
                for di, dj in dirs:
                    # print(tmp[0]+di, tmp[1]+dj)
                    if isIn(tmp[0]+di,tmp[1]+dj) and land[tmp[0]+di][tmp[1]+dj][1]<0 and abs(land[tmp[0]+di][tmp[1]+dj][0]-land[tmp[0]][tmp[1]][0])<=height:
                        # print("in")
                        land[tmp[0]+di][tmp[1]+dj][1] = gcnt
                        q.put([tmp[0]+di,tmp[1]+dj])
                # print("qsize:",q.qsize())

    print("gcnt",gcnt)
    smalls = [[1000000000 for __ in range(gcnt+1)] for _ in range(gcnt+1)]
    # calculate
    for i in range(lsize):
        for j in range(lsize):
            for di, dj in dirs:
                if isIn(i+di,j+dj) and land[i+di][j+dj][1] != land[i][j][1]:
                    tmp  = abs(land[i+di][j+dj][0] - land[i][j][0])
                    print("---------------------------")
                    print("i,j              ", i,j)
                    print("i+di,j+dj        ", i+di,j+dj)
                    print("tmp              ", tmp)
                    print("land[i+di][j+dj] ", land[i+di][j+dj])
                    print("land[i][j]       ", land[i][j])
                    if smalls[land[i+di][j+dj][1]][land[i][j][1]] > tmp:
                        smalls[land[i+di][j+dj][1]][land[i][j][1]] = tmp
                        smalls[land[i][j][1]][land[i+di][j+dj][1]] = tmp
    
    # make graph
    lines = []
    for i in range(1,gcnt+1):
        for ii in range(1,i+1):
            if i == ii: continue
            lines.append([i,ii,smalls[i][ii]])

    dots = [ False for a in range(gcnt+1)] 
    lines = sorted(lines, key=lambda x:x[2])
    cnt = 0
    print(lines)
    print(dots)
    for i in lines:
        if dots[i[0]] and dots[i[1]]:
            continue
        dots[i[0]] = dots[i[1]] = True
        answer += i[2]
        if cnt == gcnt-1:
            break
        else:
            cnt += 1

    return answer

numbers = [[[[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3],[[[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1]]

for i in numbers:
    print(solution(i[0],i[1]))
