from django.shortcuts import render
import os
import pickle
from .helper import get_random_year, get_first_10_elements, filter_empty_items, convert_genre_ids_to_names, recommend, create_tmdb_query
import pip._vendor.requests as requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

# Create your views here.
def suggestion(request):
    return render(request, 'suggestion.html')

def random(request):
    context = {}
    try:
        if request.method == 'GET':
            context['year'] = get_random_year(int(request.GET['decade']))
            api_url = create_tmdb_query(api_key=TMDB_API_KEY, year=context['year'])
            res = requests.get(api_url)
            data = res.json()['results']
            data = get_first_10_elements(data)
            for movie in data:
                movie['genre_names'] = convert_genre_ids_to_names(movie['genre_ids'])
            
            return render(request, 'random.html', {'data': data})

    except:
        pass
    return render(request, 'random.html')


def similar(request):
    context = {}
    movies_list = pickle.load(open('./model/movies.pkl', 'rb'))
    movie_titles = movies_list['title'].values

    context['titles'] = movie_titles

    if request.method == 'POST':
        movie = request.POST.get('movie')  
        recommended_movies = recommend(movie, TMDB_API_KEY)
        filtered_recommendations = filter_empty_items(recommended_movies)
        context['recommended'] = filtered_recommendations
        print(context['recommended'])
        return render(request, 'similar.html', context)

    return render(request, 'similar.html',context)

def mood(request):
    context = {}
    try:
        if request.method == 'GET':
            context['genre'] = request.GET['genre']
            context['year'] = get_random_year(int(request.GET['decade']))
            context['serviceprovider'] = request.GET['serviceprovider']
            context['lang'] = request.GET['lang']
            api_url = create_tmdb_query(api_key=TMDB_API_KEY, year=context['year'], genre=context['genre'], provider=context['serviceprovider'], language=context['lang'])
            res = requests.get(api_url)
            data = res.json()['results']
            data = get_first_10_elements(data)

            for movie in data:
                movie['genre_names'] = convert_genre_ids_to_names(movie['genre_ids'])
            
            return render(request, 'mood.html', {'data': data})

    except:
        pass
    return render(request, 'mood.html')