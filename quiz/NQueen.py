def nqueen(n):
    """
    visited 의 인덱스는 행, 값은 열을 나타낸다.
    (1, 3)에 놓은 경우, visited[1] = 3 으로 표현하겠다는 것.

    예시) n=4 이고 visited = [1, 3, 0, 2] 인 경우,
    체스판을 그려보면 아래와 같다. (1이 퀸)
    0 1 0 0  <- 여기서 인덱스를 행 이라고 가정하면, (0,1) 이 된다
    0 0 0 1  <- (1, 3)       행을 인덱스로 카운트하면
    1 0 0 0  <- (2, 0)    <- n=4일때 0, 1, 2, 3 행으로 카운트하면,
    0 0 1 0  <- (3, 2)       행 표시를 생략하고 [1, 3, 0, 2 ] 라고 표기할 수 있다

    plus 어차피 우리는 1개의 행 당 1개의 퀸만 배정이 가능하므로 2차원 배열을 1차원식으로 표기가 가능해진다
    """
    visited = [-1] * n
    cnt = 0
    answers = []

    def is_ok_on(nth_row):
        """
        n번째(nth) 행에 퀸을 놓았을 때, 올바른 수인지 검사한다.
        nth 행의 퀸 위치와, 0번째 행부터 n-1번째 행까지 놓여진 퀸의 위치를 비교한다.
        nth 행에 놓여진 퀸이 규칙을 깼다면 False 를 반환한다.
        """
        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.
        # 영상에서 n-1이라고 말하는데 오류입니다. nth_row-1까지 살펴봅니다.
        for row in range(nth_row):
            # 방금 놓여진 nth 퀸은 (nth_row, visited[nth_row]) 에 놓여져있다.
            # 각 행에 차례대로 단 한 번만 두기 때문에 행이 겹치는 것은 검사하지 않아도 된다.
            # 1) 열 번호가 겹치지는 않는지? visited[nth_row] == visited[row]: <- 같은 열에 있는가?
            # 2) 또는 대각선으로 존재하지는 않는지? nth_row - row == abs(visited[nth_row] - visited[row]) 살펴본다.
            #                               위의 코드는 x 만큼의 거리 = y만큼의 거리가 같다면 대각선에 있다는 뜻
            #                               퀸은 상, 하, 좌, 우, 대각선으로 이동가능하므로 확인하여야 한다
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False  # y2 - y1  =  x2 - x1 의 값이 같다면 대각선에 위치함을 뜻함
        return True

    def dfs(row):
        """
        row 는 퀸을 놓을 행번호를 의미한다.
        dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
        dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
        ...
        dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
        따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.
        """

        # 0 ~ n-1 행에 퀸을 모두 하나씩 두었을 때 경우의 수를 1 증가시키고 재귀탐색을 종료한다.
        if row >= n:
            # nonlocal 은 지역변수가 아님을 의미한다.
            nonlocal cnt
            cnt += 1
            print("*" * 80)  # 단순히 구분 선을 그리기위한 코드

            print(f"{cnt}번째 답 - visited: {visited}")
            grid = [['.'] * n for _ in range(n)]
            for idx, value in enumerate(visited):  # enumerate: 순서가 있는 자료형 [= 리스트, 튜플, 문자열 등]을
                grid[idx][value] = 'Q'  # 입력(값)으로 받아와 인덱스와 값을 순회하는데 사용함
            result = []  # ex) enumerate 리턴 값은 ({idx}:{value}) 으로
            for row in grid:  # 인덱스와 값을 동시에 사용할수있는 이터레이터가 됨
                print(row)
                result.append(''.join(row))
            answers.append(result)
            ################
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n):
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            visited[row] = col  # 현재 행에 퀸을 배치할 수 있는 모든 열을 찾음
            if is_ok_on(row):
                dfs(row + 1)

    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers

assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]



from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cnt = 0
        ans = []
        visited = [-1] * n

        def is_ok_on(nth_row):
            for row in range(nth_row):
                if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                    return False
            return True

        def dfs(row):
            if row >= n:
                nonlocal cnt
                cnt += 1

                grid = [['.'] * n for _ in range(n)]
                for idx, value in enumerate(visited):
                    grid[idx][value] = "Q"
                result = []
                for row in grid:
                    print(row)
                    result.append(''.join(row))
                ans.append(result)
                return

            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)

        dfs(0)
        return ans


solution = Solution()
assert solution.solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
