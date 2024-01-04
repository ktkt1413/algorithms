# 49. leetcode49. anagram
# solution: 1. 각 단어를 분해하여 재정렬
#           2. 재정렬된 단어가 딕셔너리에 없다면 추가, 있다면 해당 단어 키에 밸류값으로 어펜드
#           3. 밸류값으로 리턴

# 방법 2 가지, defaultdict를 사용하느냐 list를 사용하느냐
# 1. List 사용
#  위와 같이 입력값과 반환값 형태를 명시해주어도 되나 'from typing import List'를 한 경우에는
# 반드시 반환 값을 입력하지 않아도 된다. 파이썬3.8 버전에서는 타입힌트가 선택사항 이므로 typing모듈을 호출하여 주는 것이 좋다
# dic[] =[] <- 키, 밸류 모두 생성
# 딕셔너리에서 append()는 value 부분에 값을 할당하는 것이 디폴트

# 2. defautdict 사용시
# defaultdict는 key가 없어도 에러X, 초기생성시 설정으로 키 생성
# 그래서 key유무 체크하지X

from typing import List
from collections import defaultdict


class Anagrams:
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            anagrams = "".join(sorted(word))
            if anagrams not in dic:
                dic[anagrams] = [word]
            else:
                dic[anagrams].append(word)

        return list(dic.values())


    def dictUsage(self, strs):
        dic = defaultdict(list)
        for word in strs:
            dic["".join(sorted(word))].append(word)
        return list(dic.values())

sol = Anagrams()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result1 = sol.groupAnagrams(strs)
result2 = sol.dictUsage(strs)

print("result1:", result1)
print("result2:", result2)
