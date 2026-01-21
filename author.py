
class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] # empty list, does not need argument
    # def publish is a method to add a book to the author's list of books, using append to add to the empty book list made above
    def publish (self, title):
        if title not in self.books: # to avoid duplicates
            self.books.append(title)
        else:
            print(f'The book "{title}" is already published by {self.name}.')

    def __str__(self):
        book_list = ', '.join(self.books) or 'No books published yet' # this is the same as an if else statement as empty lists are false
        return f'{self.name}: {book_list}'


def main():

    jane_austen = Author('Jane Austen')
    jane_austen.publish('Pride and Prejudice')
    jane_austen.publish('Sense and Sensibility')
    jane_austen.publish('Sense and Sensibility')  # Attempt to publish the same book again

    print(jane_austen)  # Output: Jane Austen


    jacob = Author('Jacob Zapata')
    jacob.publish('The Great Adventure')
    jacob.publish('The Great Adventure')  # Attempt to publish the same book again
    jacob.publish('Mystery of the Lost City')
    print(jacob) 
   
main()    

    

