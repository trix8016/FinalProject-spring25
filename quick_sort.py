recursion_depth = 0

def quick_sort(books):
    global recursion_depth
    quick_sort_recursive(books, 0, len(books) - 1)

def quick_sort_recursive(books, low, high):
    global recursion_depth
    if low < high:
        pi = partition(books, low, high)
        recursion_depth += 1
        quick_sort_recursive(books, low, pi - 1)
        quick_sort_recursive(books, pi + 1, high)
        recursion_depth -= 1

def partition(books, low, high):
    pivot = books[high]['rating']
    i = low - 1
    for j in range(low, high):
        if books[j]['rating'] <= pivot:
            i += 1
            books[i], books[j] = books[j], books[i]
    books[i + 1], books[high] = books[high], books[i + 1]
    return i + 1

