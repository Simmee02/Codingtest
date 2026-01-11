def solution(clothes):
    answer = 1
    #종류에 따라 옷 묶어세기
    clothes_class = {}
    for i in range(len(clothes)):
        clothes_class[clothes[i][1]] = clothes_class.get(clothes[i][1],0) + 1 
    #조합 계산 , 입거나/안입거나로
    for num in clothes_class:
        answer = answer * (clothes_class[num]+1)
    
    return answer - 1