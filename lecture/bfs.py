# 우선 DFS 와 BFS 의 차이점을 다시 곱씹어볼게요!
#
# DFS 는 탐색하는 원소를 최대한 깊게 따라가야 합니다.
# 이를 구현하기 위해 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고,
# 가장 마지막에 넣은 노드를 꺼내서 탐색하면 됩니다. → 그래서 스택을 썼죠!
#
# BFS 는 현재 인접한 노드 먼저 방문해야 합니다.
# 이걸 다시 말하면 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고,
# 가장 처음에 넣은 노드를 꺼내서 탐색하면 됩니다.
#
# 가장 처음에 넣은 노드들..? → 큐를 이용하면 BFS 를 구현할 수 있습니다!
#
# 구현의 방법은 다음과 같습니다.
# 1. 루트 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
# 4. 2부터 반복한다.
# 5. 큐가 비면 탐색을 종료한다.


from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]