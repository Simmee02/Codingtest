def solution(arr):
    answer = []
    answer.append(arr[0])
    idx = 0
    for num in arr:
        if num != answer[idx]:
            answer.append(num)
            idx += 1
            
    return answer