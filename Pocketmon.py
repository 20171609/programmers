def solution(nums):
    nums_set = set(nums)
    
    len_set = len(nums_set)
    len_num = len(nums)
    
    if len_set >= len_num//2:
        answer = len_num//2
    else:
        answer = len_set
    
    return answer