""" First attempt to implement a fast-lookup hash table method with ISBN keys"""
from random import randint

class Book:
    def __init__(self, ISBN):#add other features later
        self.ISBN=ISBN
        self.title=str(randint(0,10000))
        self.location=None

class HashTable:
    def __init__(self, initialLength=0):
        self.table=[[]for x in range(initialLength)] #list of lists for chaining
        self.nrBooks=0
        self.primes=[2,3,5,7,11,13,17,19,23,29,31,37,41]
        
    def __len__(self):
        return len(self.table)

    def hashFunction(self, ISBN):
        """This hash function is, as far as I know, of my own creation. Given random ISBNs, the output should be random, as long as the modulus has a prime factor>41. Residues of powers of primes are random modulo other primes. 
        """
        hashValue=1
        for i in range(13):
            iter=self.primes[i]**int(ISBN[i])  #note ISBNs are strings
            hashValue=hashValue+iter 
        hashValue=hashValue%len(self) #constant time, ~13*6 multiplications
        return hashValue

    def storeBook(self, book):
        hashValue=self.hashFunction(book.ISBN)
        self.table[hashValue].append(book)
        self.nrBooks+=1
            #if nrBooks is close to length, need to expand, build method later.
            
    def lookUp(self, ISBN):
        """Constant time retrieval method
        """
        hashValue=self.hashFunction(ISBN)
        for book in self.table[hashValue]:
            if ISBN==book.ISBN:
                return book
        return False

    def search(self, parameter, value):
        """super slow search algorithm, O(len(table)) run time, does not account for duplicate entries of value with distinct ISBNs"""
        for list in self.table:
            for book in list:
                if getattr(book, parameter) ==value:
                    #alternatively: if book.__dict__[parameter]==value:
                    return book
        return False

if __name__=='__main__':
#goal below is to test the hashTable class
    database=HashTable(43*47)
    print('Generating dummy data for library database')
#generate a bunch of books with random ISBNS, enough to ensure collision
    for i in range(2000):  #1 collision guaranteed, many will occur
        ISBN=''
        for j in range(13):
            ISBN+=str(randint(0,9))
        isbn=Book(ISBN)
        #store them
        database.storeBook(isbn)

#find a collision
    print('Finding biggest collision index')
    BCIDx=0 #biggest collision index
    for index in range(len(database)):
#        for i in range(len(database.table[index])):
#            print(database.table[index][i].ISBN)
#            print(database.table[index][i].title)
#            print(database.hashFunction(database.table[index][i].ISBN))
#        print('NEXT index ')
        if len(database.table[index])>BCIDx:
            BCIDx=index
    print('Biggest collision index:', BCIDx,'number of collisions:' , len(database.table[BCIDx]))

    #store a book of known ISBN to test lookUp, 
    testBook=Book('1234567890123')
    database.storeBook(testBook)
    lookedUp=database.lookUp('1234567890123')
    if lookedUp:
        print (lookedUp.title, lookedUp.ISBN)
    else:
        print('error, book not found')
#    lookup a book that isn't there to test exception
    lookedUpx=database.lookUp('01234567890123')
    if lookedUpx:
        print (lookedUpx.title, lookedUpx.ISBN)
    else:
        print('error, book not found')

#need to set up so that program doesn't end on exception

    #search by other variables, check speed. Will need >1000 for speed to be human noticable.
    searchTitle=testBook.title
    lookedUpS=database.search('title',searchTitle)
    if lookedUpS:
        print (lookedUpS.title, lookedUpS.ISBN)
    else:
        print ('error, book not found')
