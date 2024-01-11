# leetcode.17 전화번호 문자 조합
#  dfs 재귀적 함수 사용
#  중첩함수를 사용하면 부모함수에서 선언한 변수를 자식 함수에서 사용할 수 있음

def letterCombinations(digits: str) -> list[str]:
    def dfs(index: int, path: str):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):  # dic의 key 부분이 i+1 로 한번씩 다 돌고나서
            for j in dic[digits[i]]:         # len(path) == len(digits) 가 종료되면
                dfs(i+1, path +j)            # 바로 직전 함수로 돌아가 j+1 이 시행되면서
    if not digits:                           # value의 인덱스가 순환되기 시작한다.
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
          "6": "mno", "7": "pqrs", "8":" tuv", "9": "wxyz"}
    result = []
    dfs(0,"")
    return result

print(letterCombinations("23"))