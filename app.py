
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=f86f3a1394db75bfbf193d53c4da8f16&language=en-US'.format(movie_id)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

movie_data = pickle.load(open('movies.pkl', 'rb'))
movies = movie_data
movie_titles = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_posters


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Search Movies', movie_titles)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4]) 
