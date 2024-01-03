from collections import deque
# deque - 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너 // 파이썬에서 데크 = 큐
# deque.append(x) -> 데크의 오른쪽에 x를 추가함
# deque.appendleft(x) -> 데크의 왼쪽에 x를 추가함

# stack을 활용할 때는 끝에 넣었다 붙이는 것이라 list를 사용해도 무관한데,
# que를 활용할때는 맨 앞쪽에 넣고 꺼낼때는 deque를 활용하는 것이 비용이 저렴하다


def test_problem_queue(num):
    deq = deque([ i for i in range(1, num + 1)])  # -> 1부터 num까지 숫자가 데크화 됨
    while len(deq) > 1:    # 데크가 1개가 남을때 까지
        deq.popleft()  # 왼쪽에서 꺼내 버려
        deq.append(deq.popleft()) # 버리고 난 뒤 왼쪽에 있는 것은 다시 붙여(맨마지막에-deque이므로 )
    return deq.popleft()  # 마지막 1개가 남아서 while문이 끝나면 그 값을 꺼내서 반환한다

assert test_problem_queue(6) == 4
