class Library:
    def __init__(self, library_id, set_of_books, sign_up_time, books_per_day):
        self.library_id = library_id  # There are L different libraries with IDs from 0 to L–1.
        self.set_of_books = set_of_books  # the set of books in the library,
        self.sign_up_time = sign_up_time  # the time in days that it takes to sign the library up for scanning,
        self.books_per_day = books_per_day  # the number of books that can be scanned each day from the library once
                                     # the library is signed up
        self.possible_score()  # maximum possible score

    def __str__(self):
        return "Library ID: %d\n " \
               "List of books: %s\n " \
               "Time to sign up: %d\n " \
               "Books per day: %d" % \
               (self.library_id,
                ''.join(str(i) for i in self.set_of_books),
                self.sign_up_time,
                self.books_per_day)

    def possible_score(self):  # returns the maximum possible score
        pos_score = 0
        for book in self.set_of_books:
            pos_score += book.score
        return pos_score