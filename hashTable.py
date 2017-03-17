"""Main Program File for basics review program: Library Database system
hopefully to include all first year programming concepts in the construction
and management of a library database, data structures, lists, stacks, modifiers,
all that jazz"""
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
        self.primes=[2,3,5,7,11,13,17,19,23,27,29,31,37]
        
    def __len__(self):
        return len(self.table)

    def hashFunction(self, ISBN):
        hashValue=1
        for i in range(13):
            iter=self.primes[i]**int(ISBN[i])  #note ISBNs are strings
            hashValue=hashValue+iter 
#            print(hashValue)
        hashValue=hashValue%len(self) #constant time, ~13*6 multiplications
#        print(hashValue)
        return hashValue

    def storeBook(self, book):
        hashValue=self.hashFunction(book.ISBN)
        self.table[hashValue].append(book)
        self.nrBooks+=1
            #if nrBooks is close to length, need to expand, build method later.
            
    def lookUp(self, ISBN):
        hashValue=self.hashFunction(ISBN)
        found=False
        for book in self.table[hashValue]:
            if ISBN==book.ISBN:
                found=True
                return book
                    #break for loop? Should never be very long
        if not found:
            return 'error, book not found'

    def search(self, parameter):
        return self.table[0]
#super slow search algorithm, O(len(table)) run time


if __name__=='__main__':
#goal below is to test the hashTable class
    database=HashTable(10)
    print('Generating dummy data for library database')
#generate a bunch of books with random ISBNS, enough to ensure collision
    for i in range(11):  #1 collision guaranteed, many will occur
        ISBN=''
        for j in range(13):
            ISBN+=str(randint(0,9))
        isbn=Book(ISBN)
        #store them
        database.storeBook(isbn)

#find a collision
    print('Finding collisions')

    for index in range(len(database)):
        for i in range(len(database.table[index])):
            print(database.table[index][i].ISBN)
            print(database.table[index][i].title)
            print(database.hashFunction(database.table[index][i].ISBN))
        print('NEXT index ')
    #look some up
    
    #search by other variables, check speed. Will need >1000 for speed to be human noticable.


