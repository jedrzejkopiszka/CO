# The code below is very bad. Poorly optimized, does not use OOP...:
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


def get_best_books(library, books_scanned, current_time):
    time = max_time - library.sign_up_time - current_time

    sorted_books = sorted(library.books - books_scanned, key=lambda b: -scores_of_books[b])

    return list(sorted_books)[:time*library.books_per_day]


def score(library, books_scanned, current_time, libraries_signed):
    if library in libraries_signed:
        return float('-inf')

    possible_books = get_best_books(library, books_scanned, current_time)

    score = sum([scores_of_books[book_id] for book_id in possible_books])
    score /= library.sign_up_time

    return score

def schedule():
    for iteration in range(len(libraries)):
    scores = [score(library, books_scanned, current_time, libraries_signed) for library in libraries]

    best_library = scores.index(max(scores))

    best_books = get_best_books(libraries[best_library], books_scanned, current_time)

    if best_library in libraries_signed:
        break

    current_time += libraries[best_library].sign_up_time

    if current_time >= max_time:
        break

    results_books.append(best_books)
    results_libraries.append(best_library)

    books_scanned = books_scanned.union(set(best_books))
    libraries_signed.add(libraries[best_library])
    

num_of_books = num_of_libraries = max_time = None
scores_of_books = None

libraries = []
read_from_file('input_file.txt')
print(libraries[0])
