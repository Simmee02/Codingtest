def solution(my_string, is_prefix):
    answer = 0
    len_prefix = int(len(is_prefix))

    if my_string[0:len_prefix] == is_prefix:
        answer = 1
    
    return answer