from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
# from .helper import get_movie_details

load_dotenv()

TMDB_SECRET_KEY = os.environ.get("TMDB_SECRET_KEY")

# Create your views here.
def nicolas_cage(request):
    actor_id = 2963
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_SECRET_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        processed_movies = [
            {
                'title': movie['title'],
                # 'genres': ', '.join(movie['genres']),
                'poster_path': movie['poster_path'],
                'average_vote': movie['vote_average'],
            }
            for movie in movies
        ]

        return render(request, 'nicolas_cage.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'nicolas_cage.html', {'error_message': str(e)})