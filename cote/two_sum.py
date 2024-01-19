#  리트코드 167. two_sum 2 입력 배열이 정렬됨
#  투 포인터 방법 O(n) 과 이진 탐색 O(log n) 방법이 있다

from typing import List

#  투 포인터를 사용한 O(n)의 시간 복잡도의 해결 방법. 주어진 배열이 정렬되어 있기 때문에 투 포인터 방식 가능함
class Solution:
    def twoSum(self, numbers: List[int], target: int)-> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return


#  이진 탐색(binary search)을 활용한 시간복잡도 O(log n) , 공간복잡도 O(n)을 활용

class Solutions2:
    def binarySearch(self, numbers: List[int], target: int)-> List[int]:
        for i in range(len(numbers)):

            l, r = i + 1, len(numbers) -1   #  'l = i + 1' 이진 탐색 시 l 값의 초기값을 1로 설정
            tmp = target - numbers[i]

            # 이진 탐색 시작
            while l <= r:  #  l 과 r 이 같은 경우에도 반복문을 돌리기 위해 <= 부등호를 넣어 줌
                mid = l + (r-l) // 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]

                elif numbers[mid] < tmp:
                    l = mid + 1
                elif numbers[mid] > tmp:
                    r = mid -1





