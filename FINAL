#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import folium 
from IPython.display import display, HTML, Image    # installed the eemoji, and imported all necessary things 
import requests
from ipywidgets import interact_manual
from ipywidgets import interact
import ipywidgets as wg
import random 
import emoji
#pandas and json component 
def load_campground():
    campground_df = pd.DataFrame()            #loading the csv file in a dataframe using pandas
    load_campgrounds= campground_df
    campground_df = campground_df.append(pd.read_csv("https://query.data.world/s/hs4sifxii2oajmmuz6fz2kqidqcg5p"), ignore_index=True)   
    return campground_df 

campground_df= load_campground() # needed to define this variable 

counties= list(campground_df['County'].dropna().unique())  # listing out the counties, dropping unlisted ones

def geocode(location):
    query_string= {'q': location, 'format': 'json'}    # this is how i got a map of NY state. used json to load and get data. 
    url='https://nominatim.openstreetmap.org/search'
    response= requests.get(url, params = query_string)
    response.raise_for_status()
    geodata= response.json()
    return geodata

def filter_campground(counties,campground_df):  #i filtered the caampgrounds by county so i could make a dropdown with just the counties i wanted 
    campground_by_county=campgrounds[campgrounds['County']== county]
    campground_filter = campground_by_county[campground_by_county['County'] ]
    return campground_filter # this filters them into a nice way for me to extract information from just 

campgrounds = load_campground() # needed to define this variable to get camp info 

def extract_campground_info(Location, URL): 
    info = {}
    info['County'] = county['County']
    info['Location'] = county['Location']
    info['URL'] = []
    return info       # this was to help my map and sort the information into rows. I wanted the map to just show name, but for it to print URl and county.
# component 
display(HTML("<h1> <font color='green'?>NEW YORK CAMPGROUND FINDER</h1>"))  # made my heading look pretty with novel components of font color and image upload
display(Image(url='https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/westchesterny/NYS-parks-logo-9b306e485056a36_9b306fcf-5056-a36a-07e3c4019cee28aa.png',width=300))
interact_manual = interact.options(manual=True, manual_name="Find a Campground!") # this is a novel component. changed the name of the 'run interact 'button saw it on stack overflow 

center = (42.9538,-75.5268)    #folium map upload, found the center of new york to mark it and make it start there.
the_map = folium.Map(location=center,zoom_start=7)
marker = folium.Marker(location=center, popup="This is the center")
the_map.add_child(marker)
for r in campground_df.to_records():
    marker = folium.Marker(location=[r['Y'],r['X']], popup=r['Campground'],  icon = folium.Icon(color = "green"))
    the_map.add_child(marker) # plotted the ccampgrounds out in the map in counties 
display(the_map)

@interact_manual(county=counties) #interact manual, component
def main(county):   # this is my main function to extract the data from the dataframe. if / print statements.

    if county == 'HERKIMER':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=3)      # this same function repeats for all of the counties. if i had more time, i wouldve found a way to loop through. 
        print(y)
        print(emoji.emojize('Difficulty = :blue_circle:'))     # this is the emoji part. took a lot to filter out by difficulty using entirely diff website 
    if county == 'SULLIVAN':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=2)
        print(y)
        print(emoji.emojize('Difficulty = :green_circle:'))
    if county == 'CLINTON':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=2)
        print(y)
        print(emoji.emojize('Difficulty = :black_circle:'))
    if county == 'FRANKLIN':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=5)
        print(y)
        print(emoji.emojize('Difficulty = :green_circle:'))
    if county == 'FULTON':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=3)
        print(y)
        print(emoji.emojize('Difficulty = :black_circle:'))
    if county == 'HAMILTON':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=14)
        print(y)
        print(emoji.emojize('Difficulty = :green_circle:'))
    if county == 'ST LAWRENCE':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=1)
        print(y)
        print(emoji.emojize('Difficulty = :black_circle:'))
    if county == 'ESSEX':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=8)
        print(y)
        print(emoji.emojize('Difficulty = :blue_circle:'))
    if county == 'GREENE':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=1)
        print(y)
        print(emoji.emojize('Difficulty = :black_circle:'))
    if county == 'WARREN':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=7)
        print(y)
        print(emoji.emojize('Difficulty = :blue_circle:'))
    if county == 'ULSTER':
        print(f"Here are URLs to the campsites near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=2)
        print(y)
        print(emoji.emojize('Difficulty = :black_circle:'))
    if county == 'DELAWARE':
        print(f"Here are URLs to the campsites in or near your county: ")
        campground= load_campground() 
        campground = ['Campground']
        campground_df = pd.DataFrame(campgrounds, columns=["URL"])
        y = campground_df.sample(n=2)
        print(y)
        print(emoji.emojize('Difficulty = :blue_circle:'))
    
print(emoji.emojize('This means the campground is easy to access :green_circle:')) # fun little emoji guide i made to show the scale of difficulty of access
print(emoji.emojize('This means the campground is moderate to access :blue_circle:'))
print(emoji.emojize('This means the campground is hard to access :black_circle:')) # emoji, component

slider = wg.IntSlider(value=0,
                  min=0,
                  max=5,
                  description= "Rate your Experience!",
                  )
                             # novel component, made a slider to rate the users experience in code
def number1(number):
        return number
y = wg.interact(number1, number=slider)


# In[ ]:




