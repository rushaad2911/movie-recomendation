import streamlit as stm
import pandas as pd
import pickle as pk
from thefuzz import process
import requests
import json



stm.set_page_config(
    page_title="Movie Recomendation System",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = pk.load(open("data.pickle","rb"))
similarity = pk.load(open("similarity.pickle","rb"))

def recommend(movie):
    stm.write(f'Movies similar to "{movie}"')
    movie_index = data[data['title']==movie].index[0]
    
    
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:13]
    cols = stm.columns(len(movie_list)//2)

    l1,l2 = movie_list[:6],movie_list[7:]
    
    for j in [l1,l2]:
        for col,i in zip(cols,j):
            
            movie = data.iloc[i[0]].title    
            movie_img = movie.replace(" ","%")
            movie_img = requests.get(f"https://www.omdbapi.com/?apikey=2392103&t={movie}")
            poster = json.loads(movie_img.text)
            col.image(poster['Poster'],width=150)
            
            col.text(movie)
            
            
            
            


stm.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXpobHdoaHV5bDYwYjB5dm5tYWFsdXU4MDR6aHJibnd4NzBzanlkaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7rc0qU6m5hneMsuc/giphy.gif",width=100)
stm.title("Movie Recomendation system")
name = stm.text_input("Enter Movie:", "")

if stm.button("Recomend") and name != "":
    
    
    if name in list(data['title']):
        recommend(name)
        
    else:
        
    
        movie = process.extract(name,data['title'],limit=1)
        stm.write(f"Did you mean: {movie[0][0]}")
        recommend(movie[0][0])
            
else:
    stm.write("Please enter a Movie")
          
