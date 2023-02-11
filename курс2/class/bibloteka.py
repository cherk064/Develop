class Library:
    name = "Ivan"
    surname = "Ivanov"
    grade = "10B"
    books = 100
    def __init__(self,nam="Ivan",sur="Ivanpv",gr="10B",b=0):
        self.name,self.surname,self.grade,self.books = nam, sur, gr,b
    def book_borrow(self,borrowed):
        Library.books -= borrowed
        self.books += borrowed
    def book_return(self,returned):
        Library.books += returned
        self.books -= returned
    def book_check(self):
        print("Недостача книг:",Library.books) if Library.books < 0 else print("Ok")
Vasili = Library("Vasili","Makarov","9A")
Vasili.book_borrow(10)
Library.book_check(Library)