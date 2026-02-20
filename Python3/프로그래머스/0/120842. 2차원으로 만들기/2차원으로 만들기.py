def solution(num_list, n):
    len_list = int(len(num_list)//n)
    answer = [[0]*n for _ in range(len_list)]
    temp = 0
    
    for i in range(len_list):
        for j in range(n):
            answer[i][j] = num_list[temp]
            temp += 1
    
    return answer