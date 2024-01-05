# leetcode 347. Top K Frequent Element
# 상위 K번에 해당되는 요소만 추출하여라
# sol: 새로운 딕셔너리를 만들고 결과를 보여줄 리스트를 만든다 -> 각 엘리먼트의 빈도수를 세어서 딕셔너리에 값으로 입력
# -> 딕셔너리의 값을 리스트로 만들고 내림차순으로 정렬하여 상위 K번까지 추출 되도록 한다.
#  counter.items()는 Counter 객체의 메서드로, 해당 객체에 포함된 요소들의 키와 각 키에 대한 빈도수를 튜플로 반환합니다.
#  이 메서드를 사용하면 각 키와 해당 키의 빈도수를 확인할 수 있습니다.
#  most_common() 함수 사용시 reverse를 해주지 않아도 된다
# sol-2. counter 함수 사용 / sol-3. zip & most_common() 함수 사용
from typing import List
import collections
class Frequent:
    def topKFrequent(self, nums: List[int], k: int ) -> List[int]:
        dic = {}
        result = []

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        preResult = sorted(dic.items(), key=lambda x: x[1], reverse = True)
            #  sorted함수를 사용하면 리스트(키-값,튜플)로 반환하게 됨
            #  dic.item()은 모든 (key-값)의 쌍을 담은 뷰 객체를 반환
            #  key=lambda x: x[1] 는 정렬을 x의 두번째 요소 즉, 값을 기분으로 정렬
        for i in range(k):
            result.append(preResult[i][0])

        return result

    def countWay(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        result = [ num for num , freq in count.most_common(k)]

        return result

    def chatGpt(self, nums:List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        sorted_count = count.most_common()

        result = [ num for num , freq in sorted_count[:k]]

        return result