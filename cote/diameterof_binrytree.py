#  리트 코드 테스트 543.  이진트리의 직경
#  543. Diameter of Binary Tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest: int = 0        #  longest값이 리스트나 딕셔너리와 같은 자료형이라면 중첩함수 내에서도
                            #  변수 값을 조작할 수 있으나, 변수가 숫자나 문자인 경우 불변객체이므로
                            #  중첩 함수 내에서 변수를 재할당하여 사용해야하므로 longest를 클래스 변수로 선언함
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1   #  존재하지 않는 node에 -1 값을 할당 : 노드의 높이를 0으로 시작하기 위함
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)  #  현재노드를 루트로 하는 서브트리의 최장경로
            return max(left, right) + 1    #  상태값 = 현재 노드의 좌, 우 중 더 큰값을 높이로 계산

        dfs(root)
        return self.longest
