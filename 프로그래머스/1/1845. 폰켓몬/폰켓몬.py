def solution(nums):
    answer = 0
    count = {}
    
    for mon in nums:
        count[mon] = count.get(mon,0) + 1
    
    
    if len(count) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(count)    
    
    return answer