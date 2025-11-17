class Book:
    def __init__(self,isbn,title,author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_avaliable = True

    def check_out():
        if self.is_avaliable == True:
            self.is_avaliable = False
        else:
            print()
    def check_in():
        if self.is_avaliable == False:
            self.is_avaliable =True
        else:
            print()

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self,book):
        book.check_out()
        self.borrowed_books.append(book)
    def return_book(self,book):
        book.check_in()
        self.borrowed_books.pop(borrowed_books.find(book))


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self,book):
        self.books.append(book)
    def add_member(self,member_id,name):
        self.members.append(Member(member_id,name))

    def check_out_book(isbn, member_id):
        # - processes a book checkout

    def return_book(isbn, member_id):
        pass
    #- processes a book return
    def get_available_books():
        pass
        # - returns list of available books
    def get_member_books(member_id) :
        pass
        #- returns books borrowed by a member
