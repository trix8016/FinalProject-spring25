from typing import List, Tuple

def levenshtein_distance(s1: str, s2: str) -> Tuple[int, list]:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,     # deletion
                    dp[i][j-1] + 1,     # insertion
                    dp[i-1][j-1] + 1    # substitution
                )

    return dp[m][n], dp

def find_similar_titles(books: List[dict], sample_size: int = 100) -> Tuple[str, str, float, list]:
    min_distance = float('inf')
    best_pair = None
    best_matrix = None

    sample = books[:sample_size]

    for i in range(len(sample)):
        for j in range(i + 1, len(sample)):
            title1 = sample[i]['title'].lower()
            title2 = sample[j]['title'].lower()

            distance, matrix = levenshtein_distance(title1, title2)
            normalized = distance / max(len(title1), len(title2))

            if normalized < min_distance:
                min_distance = normalized
                best_pair = (title1, title2)
                best_matrix = matrix

    return best_pair[0], best_pair[1], min_distance, best_matrix
