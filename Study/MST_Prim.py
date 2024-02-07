"""
MST: 그래프상에 존재하는 모든 노드들을 최소비용으로 연결

<< Prim 알고리즘 구현 방법 >>
1. 우선순위 큐에 임의의 시작 노드 추가
  (2 ~ 5: 우선순위 큐에 노드가가 존재할 때 까지 반복)
  2. 우선순위가 가장 높은 노드 추출 (비용이 가장 낮은)
  3. 방문 여부 확인 (이미 방문한 노드인 경우 4 ~ 5 pass)
    4. 비용 및 방문 여부 업데이트
    5. 현재 노드와 연결된 노드들을 우선순위 큐에 추가
6. 최소 비용 반환
"""

import heapq

def mst_prim(start):

    visited = [False] * len(graph)
    result = 0
    pq = []

    heapq.heappush(pq, (0, start)) # 1. 우선순위 큐에 임의의 시작 노드 추가

    while pq:
        cur_cost, cur_node = heapq.heappop(pq) # 2. 우선순위가 가장 높은 노드 추출
        if not visited[cur_node - 1]: # 3. 방문 여부 확인
            # 4. 비용 및 방문 여부 업데이트
            result += cur_cost 
            visited[cur_node - 1] = True

            # 5. 현재 노드와 연결된 노드들을 우선순위 큐에 추가
            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(pq, (next_cost, next_node))

    print(result) # 최소 비용 반환

# (비용, 노드)
# 양방향 그래프를 표현한 것이지만 단방향 그래프로 정의됨
graph = {
    1: [(2,2), (1,4), (2,3)],
    2: [(2,4), (3,3)],
    3: [(1,5), (5,6), (3,4)],
    4: [(1,5)],
    5: [(2,6)],
    6: []
}

# 양방향 그래프로 수정
for cur_node, next_nodes in graph.items():
    for cost, next_node in next_nodes:
        if (cost, cur_node) not in graph[next_node]:
            graph[next_node].append((cost, cur_node))

mst_prim(1)