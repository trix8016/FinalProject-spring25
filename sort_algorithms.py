def selection_sort(books):
    n = len(books)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if books[j]['rating'] < books[min_index]['rating']:
                min_index = j
        books[i], books[min_index] = books[min_index], books[i]
