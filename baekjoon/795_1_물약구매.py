
diss = [0]
N = 0

def allDone(visit):
    for i in range(1,len(visit)):
        if not visit[i]:
            return False
    return True

def sumMoney(c):
    answer = 0
    for i in range(1,len(c)):
        if c[i]>0:
            answer += c[i]
        else:
            answer += 1
    return answer


def recur(N,c,visit,answer):
    # print(visit)
    if allDone(visit):
        s = sumMoney(c)
        if answer > s:
            print("done",s,c)
            return s 
        else:
            print("not done",s,c)
            return answer

    for i in range(1,N+1):
        if not visit[i]:
            visit[i] = True
            for ii in diss[i]:
                if not visit[ii[0]]:
                    c[ii[0]] -= ii[1]
            print(i,"번째 after",c)
            answer = recur(N,c,visit,answer)
            for ii in diss[i]:
                if not visit[ii[0]]:
                    c[ii[0]] += ii[1]
            visit[i] = False
    return answer

def main():
    N = int(input())
    c = [0] + list(map(int,input().split(' ')))
    visit = [ False for _ in range(N+1) ]
    answer = sumMoney(c)
    print(c)

    for i in range(N):
        p = int(input())
        tmp_dis = []
        for i in range(p):
            tmp = list(map(int,input().split(' ')))
            tmp_dis.append(tmp)
        print(tmp_dis)
        diss.append(tmp_dis)
    
    print(diss)
    print(answer)
    answer = recur(N,c,visit,answer)
    print(answer)

main()
