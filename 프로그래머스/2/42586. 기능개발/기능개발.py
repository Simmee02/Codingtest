def solution(progresses, speeds):
    
    finish = []
    for p , s in zip(progresses , speeds):
        finish.append((100-p+s-1)//s)
    
    answer = []
    current = finish[0] #비교할 기준을 잡아놓고
    count = 1
    
    #기준 이후의 것들을 비교 
    for d in finish[1:]:
        if d <= current:
            count += 1
        else:
            #만약에 프로세스가 종료된다면 지금까지 카운트 했던것을 정답리스트에 넣고
            answer.append(count)
            # 기준점이 될 지점을 업데이트 
            current = d
            # 카운트 초기화
            count = 1
    #마지막 루프의 결과값을 append       
    answer.append(count)        

        ###################################################
        # idx = 0
        # next_idx = idx + 1
        # while True:
        #     if finish[idx] <= finish[next_idx]:
        #         next_idx += 1
        #     else:
        #         return True
        # answer += 
    return answer