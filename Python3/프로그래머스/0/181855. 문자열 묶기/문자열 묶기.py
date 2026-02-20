def solution(strArr):
    answer = 0
    count_dict = {}
    
    for s in strArr:
        len_str = len(s)
        count_dict[len_str] = count_dict.get(len_str,0) + 1
        
    return max(count_dict.values())