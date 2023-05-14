#write a simulation of a real life event using at least 1 random input
#reseach list indexing and enumaration 
import random
#conversation with someone? Maybe a lottery? growing up w/ choices? neighborhood library take a book leave a book
#List of books in variable library
library = ["Cinder by Merissa Meyer", 
           "Man's Search for Meaning by Victor Frankl", 
           "Perks of Being a Wallflower by Stephen Chbosky", 
           "Scythe by Neal Shusterman", 
           "Atomic Habits by James Clear", 
           "Nameless by Clair Kent",
           "The Pearl by John Steinbeck"]



#Intro lists randomely each day what books are printed from that list
def randList():
    random.shuffle(library)
    for i in enumerate(library):
        print(i)
    


#User can select which book to 'keep' and add a book to the list
def dayOne():
    print("Hello, welcome to the neighborhood 'Take a Book, Leave a Book' library.\n\nHere are today's books:\n")

def selectBook():
    book = int(input("\nTo select a book, type it's number: "))
    print(library[int(book)])

    bookNew = str(input("\nReplace " + (library[int(book)]) + " by typing the new name and author of your book: "))
    library[int(book)] = bookNew
    for i in enumerate(library):
        print(i)

def playOn():
    g = input("\nType 'y' if you'd like to revisit the neighborhood library\n\nor\nType 'n' if you'd like to exit the program:\n\n")
    if g == "y":
        dayOne()
        randList()
        selectBook()
        playOn()
    if g == "n":
        quit()
    else:
        print("\nInvalid input. Please make sure your answer is only 'y' or 'n'")
        playOn()

dayOne()
randList()
selectBook()
playOn()

#User can also look at information about the book?
