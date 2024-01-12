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
            print(node)
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)  #  현재노드를 루트로 하는 서브트리의 최장경로
            print("left,right: ", left, right)
            print("self_longest: ", self.longest)
            return max(left, right) + 1    #  상태값 = 현재 노드의 좌, 우 중 더 큰값을 높이로 계산

        dfs(root)
        return self.longest

tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree.right = TreeNode(3, TreeNode(9), TreeNode(2))

# Solution 클래스의 인스턴스 생성
solution = Solution()

# 함수 호출
result = solution.diameterOfBinaryTree(tree)

# 결과 출력
print("최장 경로 길이:", result)

# longest를 인스턴스 변수로 선언하지 않고 클래스 변수로 선언한 이유는 해당 변수가 트리 전체에서의 최장 경로를 나타내기 때문입니다. 트리의 모든 노드에서 이 값을 공유하기 위해 클래스 변수로 선언되었습니다.
# 재귀적인 함수인 dfs에서는 self.longest를 통해 각 서브트리에서의 최장 경로를 갱신하고, 최종적으로 이 값을 반환하는 diameterOfBinaryTree 함수에서는 트리 전체에서의 최장 경로를 반환합니다.
# 클래스 변수로 선언되면서 초기값이 0으로 설정되어 있기 때문에, 함수 호출이 시작될 때마다 최장 경로를 찾아서 갱신할 수 있습니다.
