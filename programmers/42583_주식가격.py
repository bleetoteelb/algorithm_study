def solution(prices):
    size = len(prices) 
    answer = [0 for i in range(size)]
    stack = []
    for i in range(0,size):
        while stack and (stack[-1][0] > prices[i]):
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
                
        stack.append((prices[i],i))
        
    while stack:
        answer[stack[-1][1]] = i - stack[-1][1]
        stack.pop()
            
    return answer
