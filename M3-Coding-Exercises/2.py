# parent class
class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre

# child class
class BlogPost(Book):
    def __init__(self, website, title, author, word_count, genre, page_views):
      self.website = website
      super().__init__(title, author, genre)
      self.word_count = word_count
      self.page_views = page_views

my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)

print(my_post.website)
print(my_post.title)
print(my_post.author)
print(my_post.word_count)
print(my_post.genre)
print(my_post.page_views)
