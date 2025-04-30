recursion_depth = 0

def merge_sort(books):
    global recursion_depth
    merge_sort_recursive(books, 0, len(books) - 1)

def merge_sort_recursive(books, left, right):
    global recursion_depth
    if left < right:
        mid = (left + right) // 2
        recursion_depth += 1
        merge_sort_recursive(books, left, mid)
        merge_sort_recursive(books, mid + 1, right)
        merge(books, left, mid, right)
        recursion_depth -= 1

def merge(books, left, mid, right):
    L = books[left:mid + 1]
    R = books[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i]['rating'] <= R[j]['rating']:
            books[k] = L[i]
            i += 1
        else:
            books[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        books[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        books[k] = R[j]
        j += 1
        k += 1
