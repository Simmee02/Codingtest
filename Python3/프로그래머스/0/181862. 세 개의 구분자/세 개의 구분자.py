def solution(myStr):
    answer = []
    new_str = ''
    
    for i in range(len(myStr)):
        if myStr[i] in ['a', 'b', 'c']:
            if new_str != '':
                answer.append(new_str)
                new_str = ''
        else:
            new_str += myStr[i]
    
    if new_str != '':
        answer.append(new_str)

    if len(answer) == 0:
        return ["EMPTY"]
        
    return answer