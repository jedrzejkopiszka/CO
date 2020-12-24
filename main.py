# Znalazłem jakies linki do githuba z tym problemem:
# https://github.com/rgab1508/hashcode
# https://github.com/Brinfer/HashCode-2020/blob/main/src/QualificationRound/Class/Library.py
# https://github.com/pgimalac/hashcode-evaluator/tree/master/2020-qualification-round

# TEST INPUT DATA:
# 6 2 7  - books, libraries, deadline
# 1 2 3 6 5 4 - scores for books
# 5 2 2  - library 0 - number of books, signup, max shipping per day
# 0 1 2 3 4 - books in library 0
# 4 3 1 - library 1 - 4 books, signup time, shipping per day
# 3 2 5 0 - books in library1

import Library
import Book

LIBRARIES = []

num_of_books, number_of_libraries, time = map(int, input().split())
scores_of_books = list(map(int, input().split()))

for library in range(number_of_libraries):
    b, time, per_day = map(int, input().split())  # Kod wczytujący dane, przebia je na ksiązki i biblioteki
    books_in_library = list(map(int, input().split()))  #
    books = [Book.Book(book, scores_of_books[book]) for book in books_in_library]  #
    LIBRARIES.append(Library.Library(library, books, time, per_day))  #
