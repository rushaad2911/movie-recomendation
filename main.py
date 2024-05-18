import streamlit as stm
import pandas as pd
import pickle as pk
from thefuzz import process



data = pk.load(open("data.pickle","rb"))
similarity = pk.load(open("similarity.pickle","rb"))

def recommend(movie):
    
    movie_index = data[data['title']==movie].index[0]
    
    
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_list:
        movie = data.iloc[i[0]].title
        url_movie = movie.replace(" ","-").lower()
        id = data.iloc[i[0]].id
        movie_img = f"https://www.themoviedb.org/movie/{id}-{url_movie}/images/posters"
        print(movie_img)
        stm.text(movie)
        stm.image(movie_img,width=400)
        
        


stm.text("Movie Recomendation system")
name = stm.text_input("Enter Movie:", "")

if stm.button("Recomend") and name != "":
    if name in list(data['title']):
        recommend(name)
    else:
        stm.text(f'Movies Similar to "{name}"')
        movie = process.extract(name,data['title'],limit=5)
        
        for i in movie:
            stm.write("> "+i[0])
else:
    stm.write("Please enter a Movie")
          
