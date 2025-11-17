class Book:
    def __init__(self,isbn,title,author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_avaliable = True

    def check_out(self):
        if self.is_avaliable == True:
            self.is_avaliable = False
        else:
            raise ValueError
    def check_in(self):
        if self.is_avaliable == False:
            self.is_avaliable =True
        else:
            raise ValueError

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self,isbn):
        self.borrowed_books.append(isbn)
    def return_book(self,isbn):
        self.borrowed_books.remove(isbn)

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    def add_book(self,isbn,title,author):
        if self.books.get(isbn) == None:
            self.books[isbn] = Book(isbn,title,author)
        else:
            print("This book has already collected by this library!")
    def add_member(self,member_id,name):
        if self.members.get(member_id) == None:
            self.members[member_id] = Member(member_id,name)
        else:
            print("you have been a member of this library!")
    # - processes a book checkout
    def check_out_book(self,isbn,member_id):
        try:
            self.books[isbn].check_out()
            self.members[member_id].borrow_book(isbn)
        except ValueError:
            print("This book is not avaliable for it has been borrowed!")
        except KeyError:
            print("This book does not exist!")
    #- processes a book return
    def return_book(self,isbn,member_id):
        try:
            self.books[isbn].check_in()
            self.members[member_id].return_book(isbn)
        except ValueError:
            print("This book has been checked in!")
        except KeyError:
            print("This book does not exist!")

    def get_available_books(self):
        return list(self.books.keys())
    #- returns books borrowed by a member
    def get_member_books(self,member_id):
        try:
            return self.members[member_id].borrowed_books
        except KeyError:
            print("This member does not exist!")
if __name__ =="__main__":
    CUHK_library = Library()
    CUHK_library.add_book("114514","Thomas's Calculus","Weir Hess")
    CUHK_library.add_book("78906","Principles Of Economics","N.Greory Mankiw")
    CUHK_library.add_book("24907","Introduction To Liner Algebra","Gillbert Strang")
    CUHK_library.add_book("50539","Learn Python The Hard Way","Zed A.Shaw")
    CUHK_library.add_member("20852085","panda_piglet")
    CUHK_library.add_member("15273","Automattic")
    CUHK_library.check_out_book("114514","20852085")
    CUHK_library.check_out_book("114514","15273")
    print(CUHK_library.get_member_books("20852085"))
    print(CUHK_library.get_member_books("15273"))
    CUHK_library.return_book("24907","20852085")
