def isAble(s,t,dic):
    si = 0
    ti = 0
    ssize = len(s)
    tsize = len(t)
    
    while(si < ssize and ti < tsize):
        if t[ti] not in dic:
            ti += 1
            continue
        if t[ti] == s[si]:
            ti += 1
            si += 1
            continue
        else:
            return False
    return True
        
def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for i in range(len(skill)):
        dic[skill[i]] = i
        
    for t in skill_trees:
        returnV = isAble(skill,t,dic)
        answer += 1 if returnV else 0

    return answer
