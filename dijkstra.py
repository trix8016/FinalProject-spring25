from collections import defaultdict
import heapq

def create_book_graph(books, max_books=100):
    graph = defaultdict(list)
    subset = books[:max_books]

    for i, book1 in enumerate(subset):
        for j, book2 in enumerate(subset[i+1:], i+1):
            weight = abs(float(book1['rating']) - float(book2['rating']))
            if weight <= 1.0:
                graph[book1['title']].append((book2['title'], weight))
                graph[book2['title']].append((book1['title'], weight))

    return graph

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def find_shortest_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]
