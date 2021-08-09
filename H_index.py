def solution(citations):
    answer = len(citations)
    citations.sort(reverse = True)
    
    if citations[0] == 0:
        return 0
    
    for i in range(len(citations)-1, 0, -1):
        if citations[i] >= answer:
            break
        
        answer -= 1
    
    return answer
