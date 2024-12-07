# importing the required liberaries
import streamlit as st
import pickle

# main Recommendation dunction
def recommend(movieName):

    movie_index = movie_list_df[movie_list_df['title'] == movieName].index[0]
    distances = similarMovies[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]

    recommendedMovies = []
    for i in movie_list:
        recommendedMovies.append(movie_list_df.iloc[i[0]].title)

    return recommendedMovies

# importing the movie dataframe from the other files
movie_list_df = pickle.load(open('movies.pkl', 'rb'))
movie_list = movie_list_df['title'].values
similarMovies = pickle.load(open('similarity.pkl', 'rb'))

# App interface
st.title("Movie Recommender System")             # header

selectedMovie = st.selectbox(                    # drop Bar  
    "Select a movie",
    (movie_list),
)

if st.button("Recommend"):                        # recommend button 
    recommendations = recommend(selectedMovie)
    for i in recommendations:
        st.write(i)
else:
    st.write("Please select a movie from the given list and click on the recommend button")  
