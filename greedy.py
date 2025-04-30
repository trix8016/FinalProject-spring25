def greedy_book_cover(books, target_authors):
  covered = set()
  selected_books = []

  while covered != target_authors:
      best_book = None
      best_coverage = set()

      for book in books:
          if 'author' not in book:
              continue
          authors = set(a.strip() for a in book['author'].split(','))
          uncovered = authors & (target_authors - covered)

          if len(uncovered) > len(best_coverage):
              best_coverage = uncovered
              best_book = book

      if not best_book:
          break

      selected_books.append(best_book)
      covered |= best_coverage

  return selected_books
