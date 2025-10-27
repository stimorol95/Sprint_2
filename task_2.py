class Movies:
   def __init__(self, movies):
      self.movies = movies

   def add_movie(self, movie):
      self.movies.append(movie)  

class Comedy(Movies):
   def __init__(self, movies):
      super().__init__(movies)

   def add_movie(self, movie):
      self.movies.append(movie)
      return f'Комедии: {self.movies}'  

class Drama(Movies):
   def __init__(self, movies):
      super().__init__(movies)

   def add_movie(self, movie):
      self.movies.append(movie)
      return f'Драмы: {self.movies}'     

comedy_list = Comedy([])
drama_list = Drama([])

print(comedy_list.add_movie('Большой куш'))
print(drama_list.add_movie('Оружейный барон'))