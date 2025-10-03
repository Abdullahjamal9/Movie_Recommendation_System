import pickle
import streamlit as st
import requests
from PIL import Image

# 🔹 Helper to load pickle from Hugging Face URL
def load_pickle_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return pickle.loads(response.content)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


# 🔹 Load logo
image = Image.open('techma.png')
st.image(image, width=120)

st.header('Film Recommendation System')

# 🔹 Load pickle files from Hugging Face Dataset repo
movies = load_pickle_from_url(
    "https://huggingface.co/datasets/Abdullahjamal984/movie-recs-data/blob/main/movie_list.pkl"
)
similarity = load_pickle_from_url(
    "https://huggingface.co/datasets/Abdullahjamal984/movie-recs-data/blob/main/similarity.pkl"
)

# 🔹 Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Input the name of a movie or choose one from the provided list",
    movie_list
)

# 🔹 Show recommendations
if st.button('Display The Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # First row
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])

    # Second row
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie_names[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie_names[6])
    with col3:
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie_names[7])
    with col4:
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie_names[8])
    with col5:
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie_names[9])
