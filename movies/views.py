from django.http import HttpResponse
from movies.models import Movies
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
import json


def all_movies(request):
   if request.method=='GET':
       movies = Movies.objects.all()
       
       try:
           page = int(request.GET.get('page_no', 1))
           page_size = int(request.GET.get('page_size', 20))
       except ValueError:
           page = 1
 
       paginator = Paginator(movies, page_size)
       try:
           movies = paginator.page(page).object_list
       except (InvalidPage, EmptyPage):
           page = 1
           movies = paginator.page(page).object_list
       data = []
       for movie in movies:
           data.append({"name": movie.name,
                        "director": movie.director,
                        "imdb_score": '{0:.1f}'.format(movie.imdb_score),
                        "genre": [x.strip() for x in (movie.genre).split(",")],
                        "99popularity": movie._99popularity
                        }) 
       return HttpResponse(json.dumps(data))
   
def search_movies(request):
    if request.method=='GET':
        word_limit = 50
        q = request.GET.get('q', '')
        q = q.strip()
        if len(q) == 0:
            return HttpResponse("[]")
        if len(q)  > word_limit:
            q = q[0:word_limit]
        
        words = [x.strip() for x in q.split()]    
        
        movies = Movies.objects.all()
        for word in words:
            movies = movies.filter(
            Q(name__startswith=word) |
            Q(name__iexact=word) |
            Q(name__icontains=word))
            
        try:
            page = int(request.GET.get('page_no', 1))
            page_size = int(request.GET.get('page_size', 20))
        except ValueError:
            page = 1
  
        paginator = Paginator(movies, page_size)
        try:
            movies = paginator.page(page).object_list
        except (InvalidPage, EmptyPage):
           page = 1
           movies = paginator.page(page).object_list 
        data = []
        for movie in movies:
           data.append({"name": movie.name,
                        "director": movie.director,
                        "imdb_score": '{0:.1f}'.format(movie.imdb_score),
                        "genre": [x.strip() for x in (movie.genre).split(",")],
                        "99popularity": movie._99popularity
                        }) 
        return HttpResponse(json.dumps(data))