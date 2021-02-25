# 프로그래머스 > 타겟 넘버(DFS 문제)

# tag: DFS, 이진트리, 재귀함수

# n개의 음이 아닌 정수 numbers
# 타겟 넘버 target
# numbers의 숫자들을 더하거나 빼서 target을 만들 수 있는 경우의 수 구하기

# Python식 풀이
from itertools import product
# product: 2개 이상의 리스트의 모든 조합을 구하는 함수

def python(numbers, target):
    _list = [(x, -x) for x in numbers]
    print(_list)
    result = list(map(sum, product(*_list)))
    return result.count(target)

# 반복문을 이용한 풀이
def solution(numbers, target):
    answer = 0
    tree = [0]
    for num in numbers:
        sub_tree = list()
        for node in tree:
            sub_tree.append(node + num)
            sub_tree.append(node - num)
        tree = sub_tree
    answer = tree.count(target)
    return answer

# 재귀 함수를 이용한 풀이
def recursive(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return recursive(numbers[1:], target + numbers[0]) + recursive(numbers[1:], target - numbers[0])

if __name__ == '__main__':
    # input: [1,1,1,1,1], 3
    # output: 5
    # input: [1,1,2,2], 2
    # output: 3
    list_ = [1,1,1,1,1]
    target = 3
    print(python(list_, target))