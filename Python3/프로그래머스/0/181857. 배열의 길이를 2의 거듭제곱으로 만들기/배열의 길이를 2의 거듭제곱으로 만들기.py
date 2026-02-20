def solution(arr):
    answer = []
    arr_len = len(arr)
    ans_len = 1
    while arr_len > ans_len: 
        ans_len *= 2
    answer = arr + [0]*(ans_len-arr_len)
    return answer