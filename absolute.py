def solution(absolutes, signs):
    answer = 0
    
    for i, j in zip(absolutes, signs):
        if not j:
            i *= -1
        
        answer += i
    
    return answer
