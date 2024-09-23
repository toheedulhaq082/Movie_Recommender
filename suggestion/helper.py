import random
import pickle
import os
import pip._vendor.requests as requests
from dotenv import load_dotenv

load_dotenv()


movies = pickle.load(open('./model/movies.pkl', 'rb'))
# movies = pd.read_csv('./model/movie.csv')
# similarity = pickle.load(open('./model/similarity', 'rb'))
TMDB_SECRET_KEY = os.environ.get("TMDB_SECRET_KEY")


def fetch_movie_data(movies):
    TMDB_BASE_URL = 'https://api.themoviedb.org/3'
    movie_data = []
    
    for movie in movies:
        search_url = f"{TMDB_BASE_URL}/search/movie?api_key={TMDB_SECRET_KEY}&query={movie}"
        response = requests.get(search_url)
        
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                for result in data['results']:
                    poster_url = f"https://image.tmdb.org/t/p/w500{result['poster_path']}" if result['poster_path'] else None
                    
                    # Append only if poster is not None
                    if poster_url:
                        movie_info = {
                            'title': result['title'],
                            'poster': poster_url,
                            'vote_average': result['vote_average'],
                        }
                        movie_data.append(movie_info)
            else:
                print(f"No results found for {movie}.")
        else:
            print(f"Error fetching data for {movie}: {response.status_code}")
    
    return movie_data


def get_random_year(start_year, current_year=2024):

    end_year = min(start_year + 10, current_year)
    return random.randint(start_year, end_year)

def get_random_year_for_disney(start_year, current_year=2021):

    end_year = min(start_year + 10, current_year)
    return random.randint(start_year, end_year)

 

def get_first_10_elements(arr):
    # ran = random.Random(range(10))
    return arr[:10]

def filter_empty_items(recommended_movies):

  return [movie for movie in recommended_movies if movie]


def get_movie_details(movie_id, api_key):
#   print(f"Fetching movie details for movie_id: {movie_id}")
  url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()

    title = data['title']
    genres = [genre['name'] for genre in data['genres']]
    poster_path = data['poster_path']
    average_vote = data['vote_average']
    return {
        'title': title,
        'genres': genres,
        'poster_path': poster_path,
        'average_vote': average_vote
    }

def convert_genre_ids_to_names(genre_ids):

     
    genre_map = {
     28: "Action",
     18: "Drama",
     35: "Comedy",
     27: "Horror",
     10749: "Romance",
     878: "Science Fiction",
     53: "Thriller",
     12: "Adventure",
     16: "Animation",
     80: "Crime",
     99: "Documentary",
     10751: "Family",
     14: "Fantasy",
     36: "History",
     10402: "Music",
     9648: "Mystery",
     10752: "War",
     37: "Western",
     10770: "TV Movie",
     9648: "Mystery",
     10749: "Romance",
     878: "Science Fiction",
     53: "Thriller",
     12: "Adventure",
     16: "Animation",
     80: "Crime",
     99: "Documentary",
     10751: "Family",
     14: "Fantasy",
     36: "History",
     10402: "Music",
     9648: "Mystery",
     10752: "War",
     37: "Western",
     10770: "TV Movie",
     10759: "Action & Adventure",
     10411: "Music Video",
     9808: "Western",
     10763: "News",
     10764: "Reality-TV",
     10765: "Sci-Fi & Fantasy",
     10766: "Soap",
     10767: "Talk",
     10768: "War & Politics",
     10769: "Anime",
     10772: "Game Show"
     }
    return [genre_map.get(genre_id, "Unknown Genre") for genre_id in genre_ids]

def recommend(movie, TMDB_API_KEY):
    for index, row in movies.iterrows():
        if row['title'] == movie:
            movie_id = row[0]
      
            base_url = "https://api.themoviedb.org/3/movie/{}/recommendations".format(movie_id)
            params = {
                "api_key": TMDB_API_KEY,
                "language": "en-US"
            }
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
      
            recommended_movies = []
            # Loop through a maximum of 5 results
            for count, result in enumerate(data["results"], start=1):
              if count > 5:
                break  
      
              recommended_movies.append({
                "title": result["title"],
                "overview": result.get("overview"),
                "poster_path": result.get("poster_path"),
                "vote_average": result.get("vote_average"),
              })
      
            return recommended_movies
  
    else:
      print(f"Movie '{movie}' not found in the dataset.")
      return []

def generate_random_number():

  return random.randint(1, 3)

def create_tmdb_query(api_key, 
                      year=None, 
                      language=None, 
                      genre=None, 
                      provider=None, 
                      include_adult=False, 
                      include_video=False, 
                      sort_by="popularity.desc", 
                      watch_region=None, 
                      certification_country=None, 
                      certification=None, 
                      certification_gte=None, 
                      certification_lte=None, 
                      primary_release_year=None, 
                      primary_release_date_gte=None, 
                      primary_release_date_lte=None, 
                      vote_average_gte=None, 
                      vote_average_lte=None, 
                      vote_count_gte=None, 
                      vote_count_lte=None, 
                      with_cast=None, 
                      with_crew=None, 
                      with_keywords=None, 
                      with_companies=None, 
                      with_origin_country=None, 
                      with_original_language=None, 
                      with_people=None, 
                      with_release_type=None, 
                      with_runtime_gte=None, 
                      with_runtime_lte=None, 
                      without_genres=None, 
                      without_keywords=None, 
                      page=generate_random_number()):
    
    base_url = "https://api.themoviedb.org/3/discover/movie"
    query = f"?api_key={api_key}&include_adult={str(include_adult).lower()}&include_video={str(include_video).lower()}"
    query += f"&sort_by={sort_by}&page={page}"
    
    if year:
        query += f"&year={year}"
    if primary_release_year:
        query += f"&primary_release_year={primary_release_year}"
    if primary_release_date_gte:
        query += f"&primary_release_date.gte={primary_release_date_gte}"
    if primary_release_date_lte:
        query += f"&primary_release_date.lte={primary_release_date_lte}"
    if genre:
        query += f"&with_genres={genre}"
    if provider:
        query += f"&with_watch_providers={provider}"
    if watch_region:
        query += f"&watch_region={watch_region}"
    if certification_country:
        query += f"&certification_country={certification_country}"
    if certification:
        query += f"&certification={certification}"
    if certification_gte:
        query += f"&certification.gte={certification_gte}"
    if certification_lte:
        query += f"&certification.lte={certification_lte}"
    if vote_average_gte:
        query += f"&vote_average.gte={vote_average_gte}"
    if vote_average_lte:
        query += f"&vote_average.lte={vote_average_lte}"
    if vote_count_gte:
        query += f"&vote_count.gte={vote_count_gte}"
    if vote_count_lte:
        query += f"&vote_count.lte={vote_count_lte}"
    if with_cast:
        query += f"&with_cast={with_cast}"
    if with_crew:
        query += f"&with_crew={with_crew}"
    if with_keywords:
        query += f"&with_keywords={with_keywords}"
    if with_companies:
        query += f"&with_companies={with_companies}"
    if with_origin_country:
        query += f"&with_origin_country={with_origin_country}"
    if with_original_language:
        query += f"&with_original_language={with_original_language}"
    if with_people:
        query += f"&with_people={with_people}"
    if with_release_type:
        query += f"&with_release_type={with_release_type}"
    if with_runtime_gte:
        query += f"&with_runtime.gte={with_runtime_gte}"
    if with_runtime_lte:
        query += f"&with_runtime.lte={with_runtime_lte}"
    if without_genres:
        query += f"&without_genres={without_genres}"
    if without_keywords:
        query += f"&without_keywords={without_keywords}"
    
    return base_url + query


