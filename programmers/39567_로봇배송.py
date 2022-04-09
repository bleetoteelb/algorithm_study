def fm(a,b,c):
    return "Time "+str(a)+": Go Straight "+str(b)+"m and turn "+str(c)

def solution(path):
    answer = []
    dirc = [] # direction change position
    rc = [['E','S'],['S','W'],['W','N'],['N','E']] # right change
    lc = [['W','S'],['S','E'],['E','N'],['N','W']] # left change
    for i in range(1,len(path)):
        if not path[i] == path[i-1]:
            for c in rc:
                if path[i-1] == c[0] and path[i] == c[1]:
                    dirc.append([i,'right'])
            for c in lc:
                if path[i-1] == c[0] and path[i] == c[1]:
                    dirc.append([i,'left'])
    pos = 0
    size = len(dirc)
    i = 0
    while(pos < size):
        if dirc[pos][0] <= i+5:
            answer.append(fm(i,(dirc[pos][0]-i)*100,dirc[pos][1]))
            i = dirc[pos][0]
            pos += 1
        else:
            i += 1

            
    print(answer)
    return answer



# ps = "EEESEEEEEENNNN"
# result = ["Time 0: Go straight 300m and turn right","Time 3: Go straight 100m and turn left","Time 5: Go straight 500m and turn left"]

ps = "SSSSSSW"
result = ["Time 1: Go straight 500m and turn right","Time 6: Go straight 300m and turn right"]
if (result == solution(ps)):
    print("YES")
else:
    print("NO")
