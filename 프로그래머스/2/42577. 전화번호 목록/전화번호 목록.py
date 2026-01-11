def solution(phone_book):
    answer = True 
    # 정렬
    phone_book.sort()
    # 앞 뒤 비교
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
            
    return answer