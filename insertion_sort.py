class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genere = genre

  def __len__(self):
    return f"{self.title}"


# perform insertion sort by title
def insertion_sort(books_arr):

  for i in range(1, len(books_arr)):
    cur_idx = i


    while cur_idx > 0 and books_arr[cur_idx].title < books_arr[cur_idx - 1].title:
      books_arr[cur_idx], books_arr[cur_idx - 1] = books_arr[cur_idx - 1], books_arr[cur_idx]
      cur_idx -= 1


