def dfs(graph, start, target, visited=None):
  if visited is None:
      visited = set()
  visited.add(start)

  if len(visited) <= 10:
      print(f"visiting node: {start}")

  if start == target:
      return True

  if start in graph:
      for neighbor in graph[start]:
          if neighbor not in visited:
              if dfs(graph, neighbor, target, visited):
                  return True
  return False
