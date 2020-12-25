# https://github.com/rgab1508/hashcode
# https://github.com/Brinfer/HashCode-2020/blob/main/src/QualificationRound/Class/Library.py
# https://github.com/pgimalac/hashcode-evaluator/tree/master/2020-qualification-round
# https://towardsdatascience.com/google-hash-code-2020-a-greedy-approach-2dd4587b6033
# https://www.linkedin.com/pulse/google-hash-code-2020-discussing-my-solution-scored-223-prateek/?articleId=6641016885955657728


# TEST INPUT DATA:
# 6 2 7  - books, libraries, deadline
# 1 2 3 6 5 4 - scores for books
# 5 2 2  - library 0 - number of books, signup, max shipping per day
# 0 1 2 3 4 - books in library 0
# 4 3 1 - library 1 - 4 books, signup time, shipping per day
# 3 2 5 0 - books in library1

import Library
import Book


def read_from_file(file_name):

    file = open(file_name, 'r').readlines()

    num_of_books, num_of_libraries, max_time = map(int, file[0].split())
    scores_of_books = list(map(int, file[1].split()))

    line = 2
    for library in range(num_of_libraries):
        num_of_books_in_lib, sign_up_time, books_per_day = map(int, file[line].split())
        books_in_library = list(map(int, file[line+1].split()))
        line += 2

        books = [Book.Book(book, scores_of_books[book]) for book in books_in_library]
        libraries.append(Library.Library(library, books_in_library, sign_up_time, num_of_books_in_lib, books_per_day))


libraries = []
read_from_file('input_file.txt')
print(libraries[0])
