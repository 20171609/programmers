def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        result = ""
        for j in range(n-1, -1, -1):
            check = False
            if arr1[i] >= 2 ** j:
                arr1[i] -= 2 ** j
                result += "#"
                check = True
    
            if arr2[i] >= 2 ** j:
                arr2[i] -= 2 ** j
                if not check:
                    result += "#"
                check = True
            
            if check:
                continue
            
            result += " "
        
        answer.append(result)
        
    return answer
