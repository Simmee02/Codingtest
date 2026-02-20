def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
        #numbers.insert(0, numbers.pop())
    else:
        answer = numbers[1:] + [numbers[0]]
        #numbers.append(numbers.pop(0))
    return answer