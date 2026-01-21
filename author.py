
class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] # empty list, does not need argument
    # def publish is a method to add a book to the author's list of books, using append to add to the empty book list made above
    def publish (self, title):
        
        self.books.append(title)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No books published yet' # this is the same as an if else statement as empty lists are false
        return f'{self.name}: {book_list}'

jane_austen = Author('Jane Austen')
jane_austen.publish('Pride and Prejudice')
jane_austen.publish('Sense and Sensibility')

print(jane_austen)  # Output: Jane Austen


jacob = Author('Jacob Zapata')
print(jacob) 
   
    
    

