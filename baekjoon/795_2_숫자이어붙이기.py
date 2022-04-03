MOD = 1000000007
N, Q = map(int,input().split(' '))
A = ['0'] + input().split(' ')
lines = [0] + [ [] for _ in range(N) ]
visit = [False] + [ False for _ in range(N) ]

def getMOD(l):
    return str(int(l) % MOD)
    
for i in range(N-1):
    f,t = map(int,input().split(' '))
    lines[f].append(t)
    lines[t].append(f)
print("A",A)
print("lines",lines)

def recur(x,y,txt):
    print("XXXXXXXXXXXXXXXXXXX  ",x,y,txt)
    found = False
    txt += A[x]
    print("txt: ",txt)
    for d in lines[x]:
        print("d",d)
        if d == y:
            print(getMOD(txt+A[d]))
            return True
        if not visit[d]:
            visit[d] = True
            found = recur(d,y,txt)
            visit[d] = False
        if found:
            return True
        print("no...",d)

for i in range(Q):
    print("---------------------------",i)
    visit = [False] + [ False for _ in range(N) ]
    x,y = map(int,input().split(' '))
    if x == y:
        print(getMOD(A[x]))
        continue
    visit[x] = True
    recur(x,y,'')
