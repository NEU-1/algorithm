from collections import deque

def topological_sort(graph, indegree, n):
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        result.append(curr)

        for nxt in graph[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return result if len(result) == n else []


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        seq = list(map(int, input().split()))[1:]
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i + 1])
            indegree[seq[i + 1]] += 1

    result = topological_sort(graph, indegree, n)

    if result:
        for i in result:
            print(i)
    else:
        print(0)


if __name__ == "__main__":
    main()
