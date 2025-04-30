from typing import List, Dict, Tuple
import numpy as np

def cosine_similarity(book1: Dict, book2: Dict) -> float:
    vec1 = np.array([float(book1['rating']), float(book1['pages']) / 1000])
    vec2 = np.array([float(book2['rating']), float(book2['pages']) / 1000])

    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    return dot / (norm1 * norm2) if norm1 * norm2 != 0 else 0

def find_k_nearest_neighbors(books: List[Dict], target_book: Dict, k: int = 5) -> List[Tuple[Dict, float]]:
    similarities = []
    for book in books:
        if book['isbn'] != target_book['isbn']:
            sim = cosine_similarity(book, target_book)
            similarities.append((book, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:k]
