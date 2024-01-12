#  leetcode46. 순열문제 permutations

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(pair, n):
            if len(pair) == n:
                answer.append(pair[:])
                return

            for i in nums:
                if i not in pair:
                    pair.append(i)
                    dfs(pair, n)
                    pair.pop()  #  백트레킹을 하기위한 과정, answer에 어펜드 된 i를 pair에서 제거해줌
                                #  이 과정을 통해 첫번째 자리에 i로 시작하는 pair는 없게 됨
        dfs([],len(nums))  #  dfs 함수가 정의되기 전에 호출되면 NameError 발생할 수 있음

        return answer