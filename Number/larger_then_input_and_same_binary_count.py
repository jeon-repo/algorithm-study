# 십진수를 이진수로 변환
def convert_to_bin(decimal: int):
    temp_list = list()
    while decimal >= 1:
        if decimal % 2 == 0:
            temp_list.append('0')
        else:
            temp_list.append('1')
        decimal //= 2
    temp_list.reverse()
    binary = ''.join(temp_list)

    return list(binary)

# 입력된 100만 이하의 십진수를 이진수로 변환 했을 때,
# 1의 갯수가 같으면서 입력된 수보다 큰, 가장 작은 수를 구하기
# input = 78
# 78 < output
def solution(n):
    if n <= 1000000:
        answer = n
        ont_n = convert_to_bin(n).count('1')
        while 1:
            answer += 1
            if convert_to_bin(answer).count('1') == ont_n:
                break

        print(f'in: {n}, out: {answer}')
        return answer
    else:
        return '100만 이하의 자연수를 입력해주세요.'
        
if __name__ == '__main__':
    # 78 -> 83
    # 15 -> 23
    # 99 -> 101
    while 1:
        test = input()
        if test == 'exit()':
            break
        print(solution(int(test)))