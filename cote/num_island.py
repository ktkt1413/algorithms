def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]  #  보통 상->하->좌->우
    dy = [1, -1, 0, 0]  #     y+1/y-1/x+1/x-1
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'  # 해당 그리드 좌표 -> 0을 만들어라
                for i in range(4):  # dx, dy 내의 인덱스가 3까지 있음
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3