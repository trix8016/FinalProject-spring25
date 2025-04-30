import time
from typing import List, Dict, Optional

def linear_search(books: List[Dict], target_isbn: str) -> Optional[Dict]:
    start_time = time.time()
    for book in books:
        if str(book.get('isbn')) == target_isbn:
            print(f"Linear Search Time: {(time.time() - start_time) * 1000:.2f} ms")
            return book
    print(f"Linear Search Time: {(time.time() - start_time) * 1000:.2f} ms")
    return None

def binary_search(books: List[Dict], target_isbn: str) -> Optional[Dict]:
    start_time = time.time()
    left, right = 0, len(books) - 1
    while left <= right:
        mid = (left + right) // 2
        current_isbn = str(books[mid]['isbn'])
        if current_isbn == target_isbn:
            print(f"Binary Search Time: {(time.time() - start_time) * 1000:.2f} ms")
            return books[mid]
        elif current_isbn < target_isbn:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Binary Search Time: {(time.time() - start_time) * 1000:.2f} ms")
    return None
