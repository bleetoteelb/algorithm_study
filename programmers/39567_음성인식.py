import re

def solution(call):
    answer = call
    getA = [ False for _ in range(len(answer)) ]
    c = call.lower()
    # print(answer)
    # print(c)
    size = len(c)
    dic = {}
    for i in range(size):
        for ii in range(i,size):
            if c[i:ii+1] in dic:
                dic[c[i:ii+1]] += 1
            else:
                dic[c[i:ii+1]] = 1
    # print(dic)
    # print(max(dic,key=dic.get))
    maxCnt = dic[max(dic,key=dic.get)]
    # print(list(dic))
    filtered = [a[0] for a in dic.items() if a[1]==maxCnt]
    filtered = sorted(filtered,key=lambda x:len(x),reverse=True)

    # print("FFFFFFFFFF",filtered)
    # print(maxCnt)
    for i in filtered:
        # print('-----',i)
        first = True
        # size1 =
        for s in re.finditer(i,c):
            # print(s.span()[0],s.span()[1])
            if first and getA[s.start()]:
                break
            first = False
            for j in range(s.span()[0],s.span()[1]):
                getA[j] = True

    answer = ''.join([ answer[a] for a in range(len(answer)) if not getA[a] ])
    return answer

ins = ["abcabcdefabc","abxdeydeabz","abcabca","ABCabcA"]
# print(solution(ins[2]))
for i in ins:
    print(solution(i))
