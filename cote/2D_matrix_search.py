#  리트코드 240.  2D 행렬 검색 2
#  타겟과 각 행의 마지막 값을 비교하면 비교적 쉽게 풀수 있음

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def binary_search(idx):
            left, right = 0, len(matrix[0]) -1
                            #  위의 값은 첫번째 행의 마지막 인덱스를 가리킴
            while left <= right:
                mid = (left + right) //2

                if matrix[idx][mid] == target:
                    return True
                elif matrix[idx][mid]  <  target:
                    left = mid + 1
                elif matrix[idx][mid] > target:
                    right = mid - 1
            return False

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            if binary_search(i):
                return True

        return False