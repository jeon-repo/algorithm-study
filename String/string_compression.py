inputData = {
    'aabbaccc': 7,
    'ababcdcdababcdcd': 9,
    'abcabcdede': 8,
    'abcabcabcabcdededededede': 14,
    'xababcdcdababcdcd': 17
}

# 문제 의도 : 얼마의 길이로 압축을 하는게 가장 효율적인가
def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    for leng in range(1, (len(s)//2)+1):
        string = ''
        s_pos = 0
        count = 1
        while s_pos < len(s):
            e_pos = s_pos + leng
            if s[s_pos:e_pos] == s[e_pos:e_pos+leng]:
                count += 1
            elif count <= 1:
                string += s[s_pos:e_pos]
            else:
                string += str(count) + s[s_pos:e_pos]
                count = 1
            s_pos += leng
        if len(string) < answer:
            answer = len(string)
    
    return answer

### 테스트 실행
# for st in list(inputData.keys()):
#     print(solution(st))

######################################################################
### 참신한 풀이가 있어서 참조

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution2(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

# for x in a:
#     print(solution(x))
text = a[1]
print(list(range(1, (len(text) // 2) + 1)) + [len(text)])