#The following code  checks the process of a library in register of books
class Book():
    __size = "17x24"
    pages=0
    salesPrice = 0
    wheight =0
    __PricePerPage = 0
    __sizePerPage = 0
    title = ''
    bookCover=''
    URL=''
    ISBM=''
    status='unregistered'

    def __init__(self):
        self.__size="17x24"
        self.__PricePerPage=300
        self.__sizePerPage=0.8
    
    def RecordBook(self):
        status = 'Registered'
        return status
    
    def pricexPage(self):
        return self.__PricePerPage
    
    def sizexPage(self):
        return self.__sizePerPage
    
    def sizeBook(self):
        return self.__size
    
def DataBooks(Book,name,numberPages,Cover,URLlibro,ISBMlibro):
    Book.salesPrice= Book.pricexPage()*numberPages
    Book.wheight=Book.sizexPage()*numberPages
    Book.title=name 
    Book.bookCover = Cover
    Book.URL=URLlibro
    Book.ISBM=ISBMlibro

def ReceiveData(Book):
    name=input("Title Book: ")
    numberPages=int(input("Number Pages: "))
    Cover=input("Book Cover: ")
    URLlibro = input("URL Book: ")
    ISBMlibro = input("ISBM Book: ")
    print('*****************************************')
    DataBooks(Book,name,numberPages, Cover, URLlibro, ISBMlibro)


def ShowDataBook(Book):
    print(f'Size: {Book.sizeBook()}')
    print(f'Pages: {Book.pages}')
    print(f'Sale price : {Book.salesPrice}')
    print(f'weight: {round(Book.wheight,2)}')
    print(f'Price X page: {round(Book.salesPrice,2)} COP')
    print(f'Weight X page: {Book.sizexPage()} gms')
    print(f'Title: {Book.title}')
    print(f'Cover: {Book.bookCover}')
    print(f'URL: {Book.URL}')
    print(f'ISBM: {Book.ISBM}')
    print(f'Status: {Book.status}')
    print('*****************************************')

#Execution test

libro1 = Book()
libro2 = Book()

print("DATOS LIBRO 1")
ReceiveData(libro1)

print("DATOS LIBRO 2")
ReceiveData(libro2)

ShowDataBook(libro1)
ShowDataBook(libro2)