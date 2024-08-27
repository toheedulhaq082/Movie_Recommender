# from dotenv import load_dotenv
# import os
# import requests

# load_dotenv()

# TMDB_SECRET_KEY = os.environ.get("TMDB_SECRET_KEY")


# def fetch_and_sort_movies(actor_id):

#     api_key = "TMDB_SECRET_KEY"  
#     movies = []

#     for page in range(1, 1):
#         try:
#             url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_people={actor_id}&sort_by=popularity.desc&page={page}"
#             response = requests.get(url)
#             response.raise_for_status()  
#             data = response.json()
#             movies.extend(data['results'])
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching data for page {page}: {e}")
#             # You can handle the error here, like logging it

#     # Sort the movies by popularity in descending order
#     sorted_movies = sorted(movies, key=lambda x: x['popularity'], reverse=True)

#     # Return the top 20 movies
#     return sorted_movies[:20]