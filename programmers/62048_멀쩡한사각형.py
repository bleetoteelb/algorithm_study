from math import gcd

def solution(w,h):
    lcm = w*h // gcd(w,h)
    cropped = (1 + lcm/w + lcm/h - 2) * h/(lcm/w)
    
    answer = w*h - cropped
    return answer
