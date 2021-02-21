def pressed(s,i):
    returnV = []
    target = s[0:i]
    pos = i
    cnt = 1
    while(True):
        comp = s[pos:pos+i]
        #print("1 << target:"+target+"/comp:"+comp+"/pos:"+str(pos))
        if target == comp:
            cnt += 1
        else:
            if cnt > 1:
                returnV.append(cnt)
            returnV.append(target)
            target = comp
            cnt = 1
        pos += i
        if pos+i>len(s):
            if cnt > 1:
                returnV.append(cnt)
            returnV.append(target)
            returnV.append(s[pos:])
            break
            
    return len("".join(map(str,returnV)))
    
def solution(s):
    answer = 100000
    for i in range(1,len(s)//2+2):
        returnV = pressed(s,i)
        answer = returnV if answer>returnV else answer
    return answer
