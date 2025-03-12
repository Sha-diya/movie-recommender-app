import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os
load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
# Fetch poster functions
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

# Recommender function
def recommender(movie):
    if movie not in movie_titles:
        return ["Movie not found!"], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_poster


# Streamlit app title
st.title("Movie Recommender System")

# Load the movies and similarity data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract movie titles
movie_titles = movies['title'].values

# Movie selection
selected_movie_name = st.selectbox("Which movie would you like?", movie_titles)

# Recommendation button
if st.button("Recommend"):
    names, posters = recommender(selected_movie_name)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster, width=150 ,use_container_width=True)