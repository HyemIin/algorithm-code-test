def solution(numbers):
    number = []
    for i in numbers:
        number.append(str(i))
    
    srt = sorted(number, key=lambda x : (x * 3),reverse = True)
    answer = "".join(srt)
    return str(int(answer))