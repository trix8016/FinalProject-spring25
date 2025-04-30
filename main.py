import json
import time
from search import linear_search, binary_search
from sort_algorithms import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from hash_table import HashTable
from dfs import dfs
from avl_tree import AVLTree
from dijkstra import create_book_graph, dijkstra, find_shortest_path
from greedy import greedy_book_cover
from dynamic_programming import find_similar_titles
from knn_algorithm import find_k_nearest_neighbors

def load_books(filename="books.json"):
    try:
        with open(filename, "r") as f:
            books = json.load(f)
            for book in books:
                if "rating" not in book:
                    book["rating"] = 0.0
                if "pages" not in book:
                    book["pages"] = 200  # default if missing
            return books
    except Exception as e:
        print(f"error loading books: {e}")
        return []

def display_books(books, count=10):
    print("-" * 40)
    for i, book in enumerate(books[:count]):
        print(f"{i + 1}. {book['title']} (rating: {book['rating']})")
    print("-" * 40)

def create_graph_by_author(books):
    graph = {}
    author_to_books = {}

    for book in books:
        if 'author' in book:
            authors = book['author'].split(',')
            for author in authors:
                author = author.strip()
                author_to_books.setdefault(author, set()).add(book['title'])

    for book_set in author_to_books.values():
        for book1 in book_set:
            for book2 in book_set:
                if book1 != book2:
                    graph.setdefault(book1, []).append(book2)

    return graph

def bfs(graph, start, target):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(f"visiting node: {node}")
        if node == target:
            return True
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return False

def main():
    books = load_books()

    # --- linear search ---
    print("\n--- linear search ---")
    result = linear_search(books, "9780439554939")
    if result:
        print(f"found: {result['title']}")
    else:
        print("book not found")

    # --- binary search ---
    print("\n--- binary search ---")
    books.sort(key=lambda x: str(x['isbn']))
    result = binary_search(books, "9780439554939")
    if result:
        print(f"found: {result['title']}")
    else:
        print("book not found")

    # --- selection sort ---
    print("\n--- selection sort (by rating) ---")
    selection_sort(books)
    display_books(books)

    # --- merge sort ---
    print("\n--- merge sort (by rating) ---")
    merge_books = books.copy()
    merge_sort(merge_books)
    display_books(merge_books)

    # --- quick sort ---
    print("\n--- quick sort (by rating) ---")
    quick_books = books.copy()
    quick_sort(quick_books)
    display_books(quick_books)

    # --- chapter 5 hash tables ---
    print("\n--- chapter 5 hash tables ---")
    hash_table = HashTable()
    for book in books:
        hash_table.insert(book['title'], book['rating'])

    lookup_title = "matilda"
    start_lookup = time.time()
    rating = hash_table.get(lookup_title)
    end_lookup = time.time()

    if rating is not None:
        print(f"rating for '{lookup_title}': {rating}")
    else:
        print(f"'{lookup_title}' not found in hash table")
    print(f"lookup time: {(end_lookup - start_lookup):.6f} seconds")

    start_delete = time.time()
    hash_table.delete(lookup_title)
    end_delete = time.time()
    print(f"deleted '{lookup_title}' from hash table")
    print(f"deletion time: {(end_delete - start_delete):.6f} seconds")

    if hash_table.get(lookup_title) is None:
        print(f"confirmed: '{lookup_title}' no longer exists in hash table")

    # --- chapter 6 breadth first search ---
    print("\n--- chapter 6 breadth first search ---")
    graph = create_graph_by_author(books)

    start_node = "les misérables"
    target_node = "the hunchback of notre dame"

    print(f"starting bfs from '{start_node}' to '{target_node}'")
    found = bfs(graph, start_node, target_node)

    if found:
        print(f"path found from {start_node} to {target_node}")
    else:
        print(f"no path found from {start_node} to {target_node}")

    # --- chapter 7 depth first search ---
    print("\n--- chapter 7 depth first search ---")
    print(f"starting dfs from '{start_node}' to '{target_node}'")
    found = dfs(graph, start_node, target_node)

    if found:
        print(f"path found from {start_node} to {target_node} using dfs")
    else:
        print(f"no path found from {start_node} to {target_node} using dfs")

    # --- chapter 8 avl trees ---
    print("\n--- chapter 8 avl trees ---")
    print("building avl tree with subset of books...")

    avl_tree = AVLTree()
    subset_books = books[:100]

    for book in subset_books:
        avl_tree.insert_book(book)

    sorted_books = []
    avl_tree.inorder_traversal(avl_tree.root, sorted_books)

    print("\nfirst 20 books in order of rating (avl tree inorder traversal):")
    display_books(sorted_books, 20)

    # --- chapter 9 dijkstra's algorithm ---
    print("\n--- chapter 9 dijkstra's algorithm ---")
    book_graph = create_book_graph(books[:100])

    start_book = books[0]['title']
    end_book = books[-1]['title']

    print(f"\nfinding shortest path between:")
    print(f"start: {start_book}")
    print(f"end: {end_book}")

    distances, previous = dijkstra(book_graph, start_book)

    if end_book in distances and distances[end_book] != float('infinity'):
        path = find_shortest_path(previous, start_book, end_book)
        print("\nshortest path found:")
        for i, book in enumerate(path):
            rating = next(b['rating'] for b in books if b['title'] == book)
            print(f"{i+1}. {book} (rating: {rating})")
        print(f"\ntotal path weight: {distances[end_book]:.2f}")
    else:
        print("\nno path found between these books")

    # --- chapter 10 greedy algorithm ---
    print("\n--- chapter 10 greedy algorithm ---")
    target_authors = {
        "victor hugo",
        "roald dahl",
        "katherine paterson",
        "e b white",
        "louis sachar"
    }

    selected = greedy_book_cover(books, target_authors)

    if selected:
        print("\nbooks selected to cover all target authors:")
        for book in selected:
            print(f"- {book['title']} by {book.get('author', 'unknown')}")
    else:
        print("\ncould not cover all authors with available books")

    # --- chapter 11 levenshtein distance ---
    print("\n--- chapter 11 levenshtein distance ---")
    print("finding most similar titles based on edit distance")

    t1, t2, dist, matrix = find_similar_titles(books, 100)

    print(f"\ntitle 1: {t1}")
    print(f"title 2: {t2}")
    print(f"normalized distance: {dist:.2f}")

    print("\nfirst 5x5 of dp matrix:")
    for row in matrix[:5]:
        print(row[:5])

    # --- chapter 12 knn algorithm ---
    print("\n--- chapter 12 knn algorithm ---")
    print("finding books most similar to the first one")

    target = books[0]
    neighbors = find_k_nearest_neighbors(books, target, k=5)

    print(f"\ntarget: {target['title']} (rating: {target['rating']} | pages: {target['pages']})")
    print("\ntop 5 similar books:")
    for book, score in neighbors:
        print(f"{book['title']} (similarity: {score:.2f})")

if __name__ == "__main__":
    main()
