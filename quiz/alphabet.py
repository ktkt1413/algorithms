import string

def getIdxNaive(word):
    result = [-1]*len(string.ascii_lowercase)
    # O(N^2)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:     # result[j] 가 소문자 알파벳이고, 해당 알파벳이 word 내에 있다면
                result[j] = i                      # i 를 출력해라 (word 내의 해당 알파벳의 인덱스), 없다면 -1을 출력
    print(' '.join([str(num) for num in result]))  # 숫자를 문자로 바꾸고, ' ' 로 구별하여 합쳐서 출력해라

def getIdx(word):
    # point1. ord ( 문자열 -> 숫자)
    # point2. O(N^2) -> O(N) , for문이 2번에서 1번 사용되었으므로
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97    # 소문자a 의 아스키 코드가 97이므로 -97을 함으로써 인덱스를 알수있음
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))




get_idx_naive("baeckjoon")
get_idx("baeckjoon")