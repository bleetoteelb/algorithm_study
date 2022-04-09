import re

def solution(ts, vs):
    answer = ts
    dic = {}
    visit = {}
    # make it dic
    for i in range(len(vs)):
        dic[vs[i][0]] = vs[i][1]
        visit[vs[i][0]] = False

    # check cycle and convert to end
    for i in range(len(vs)):
        tmp = vs[i][1]
        while(re.match(r'{[a-z]*}',tmp)):
            tmp = re.sub('[{}]','',tmp)
            if not tmp in dic:
                tmp = '{'+tmp'}'
                break
            if visit[tmp] or dic[tmp] == '!!!':
                tmp = '!!!'
                break
            visit[tmp] = True
            if tmp in dic:
                tmp = dic[tmp]
        dic[vs[i][0]] = tmp
        for k in visit.keys():
            visit[k] = False
    for i in dic.items():
        if not i[1] == '!!!':
            answer = re.sub('{'+i[0]+'}',i[1],answer)
    return answer


tstring = ["this is {template} {template} is {state}",
        "this is {template} {template} is {state}",
        "this is {template} {template} is {state}",
        "this is {template} {template} is {state}",
        "{a} {b} {c} {d} {i}"]

variables = [[["template", "string"], ["state", "changed"]],
        [["template", "string"], ["state", "{template}"]],
        [["template", "{state}"], ["state", "{template}"]],
        [["template", "{state}"], ["state", "{templates}"]],
        [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]]
# variables = [["template", "{state}"], ["template1", "{state}"], ["state", "{temp}"],["temp","{state}"]]
# variables = [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]] 

for i,j in zip(tstring,variables):
    print(solution(i,j))

