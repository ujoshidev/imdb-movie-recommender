# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:33:21 2022

@author: utkar
"""

import pickle
import streamlit as st

def recommend_movie(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Title)

    return recommended_movie_names
##https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bestteenmovies-1612822987.jpg?crop=1xw:1xh;center,top&resize=1200:*
page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://res.cloudinary.com/jerrick/image/upload/c_scale,q_auto/kjtno13kgjwr1qusuz3h.png");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

original_title = '<p style="font-family:sans-serif; color:RED; font-size: 42px;">Movie Recommendation System</p>'
st.markdown(original_title, unsafe_allow_html=True)
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names = recommend_movie(selected_movie)
    for i in recommended_movie_names:
        return_data = f'<p style="font-family:fantasy; color:CYAN; font-size: 28px;">{i}</p>'
        st.markdown(return_data,unsafe_allow_html=True)