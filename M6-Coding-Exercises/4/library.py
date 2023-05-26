class Library:
  def __init__(self):
    self.books = []
    self.fiction = []
    self.nonfiction = []
    
  def add_book(self, book):
    '''Takes a Book object and adds it to self.books'''
    self.books.append(book)
    
  def search_title(self, title):
    '''Takes a string and returns a Boolean'''
    has_book = False
    for book in self.books:
      if title.lower() == book.title.lower():
        has_book = True
    return has_book
  
  def search_author(self, author):
    '''Takes a string and returns a list of Book objects'''
    author_books = []
    for book in self.books:
      if book.author.lower() == author.lower():
        author_books.append(book)
    return author_books
    
  def sort_books(self):
    '''Helper method for sort_fiction and sort_nonfiction'''
    self.fiction = self.sort_fiction()
    self.nonfiction = self.sort_nonfiction()
    
  def sort_fiction(self):
    '''Return list of Book objects where the genre is fiction'''
    fiction_books = []
    for book in self.books:
      if book.genre.lower() == 'fiction':
        fiction_books.append(book)
    return fiction_books
    
  def sort_nonfiction(self):
    '''Return list of Book objects where the genre is nonfiction'''
    nonfiction_books = []
    for book in self.books:
      if book.genre.lower() == 'nonfiction':
        nonfiction_books.append(book)
    return nonfiction_books
