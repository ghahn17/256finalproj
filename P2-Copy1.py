#!/usr/bin/env python
# coding: utf-8

# # IST256 Project Deliverable 2 (P2)
# 
# ## Phase 2: Beta Version
# 
# In this step you should create a first working draft of the completed program i.e. the "Beta" version; Provide live demo of your running program to your small group instructor for real-time feedback.
# 
# **IMPORTANT**: Don't forget to journal your work on the project as it factors into the evaluation of your work!

# ### Step 1: What is Your Idea, Again?
# 
# Please reiterate your project idea below (you can copy it from P1).
# 
# `--== Double-click and put the title or brief description of your project below  ==--`
# create a program where a user can input a outdoor activity and a location, or the program will fetch their current location and will display information and photos for outdoor recreation locations including hiking and mountain biking trails, campgrounds, ski resorts, ATV trails, and more. The program will return trail length, yes/no if there is parking, the distance from their input location.The data returned will be organzied neatly on the page fpr the user to access easily and visually appealing. From there, a user can get more information on the trail/location itself and be directed to more information about the place. I will use information from previous labs and use an api key from rapid api ot create this. The api key will be helpful because i can use dictionaries to categorize the information and the locate it when the location and activity is called. my end product i am hoping to make it look pretty with displays and widgets. The api key i am getting from rapid api has endpoints and urls listed on the site and and contains categories to make the data into smaller lists and even the possibility of dictionaries. I am hoping that my program is able to combine all of my skills learned this semester and then properly apply them to this project. 
# 

# ### Step 2: Problem Analysis
# 
# Complete the problem analysis for your project. What are the major steps? How does the program flow from the user's experience?
# 
# Inputs:
# 
# ```
# TODO: Inputs
# nonuser: trail data, map with marked location, state/city data 
# user: desired outdoor activity(search term), location, how far they are willing to travel
# ```
# 
# Outputs:
# 
# ```
# TODO: Outputs
# will display list of activities based on inputs, with options to get directions, and information 
# ```
# 
# Algorithm (Steps in Program):  
# 
# ```
# TODO:Steps Here
# build trail/outdoor activity data set
# build map/ location 
# list of states drop down
# search input 
# radius? (still trying to figure out how to do this)
# 
# ```

# In[18]:


api_key= 'd6d20869a4msh34cebacbb55ab704p1ec73fjs'
api_url= 'https://trailapi-trailapi.p.rapidapi.com/'


# In[19]:


import pandas as pd
import json
import requests

url = "https://trailapi-trailapi.p.rapidapi.com/"
querystring = {"q-activities_activity_type_name_eq":"hiking","radius":"25","q-state_cont":"California","q-country_cont":"Australia","q-city_cont":"Denver","lon":"-105.2","limit":"25","lat":"34.1"}
headers = {
    'x-rapidapi-key': "d6d20869a4msh34cebacbb5ab704p1ec73fjsnf5efc35efba9",
    'x-rapidapi-host': "trailapi-trailapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

def GetActivityInfo():
    response = requests.get('https://trailapi-trailapi.p.rapidapi.com/')
    data_dict = response.json()
    activity = data_dict
    return activity
GetActivityInfo()


# In[16]:


import requests

url = "https://trailapi-trailapi.p.rapidapi.com/trails/map/%7Bid%7D/gpx/"

headers = {
    'x-rapidapi-key': "d6d20869a4msh34cebacbb5ab704p1ec73fjsnf5efc35efba9",
    'x-rapidapi-host': "trailapi-trailapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

def GetActivityInfo():
    response = requests.get('https://trailapi-trailapi.p.rapidapi.com/trails/map/%7Bid%7D/gpx/')
    data_dict = response.json()
    activity = data_dict
    return activity
GetActivityInfo()


# In[17]:


import json 

r = requests.get('https://trailapi-trailapi.p.rapidapi.com/')
x = r.json()
df = pd.read_json(json.dumps(x))


# ### Step 3: Your Code Solution
# 
# You may write your code in several cells, but place the complete, final working copy of your code solution within this single cell below. Only the within this cell will be considered your solution. Any imports or user-defined functions should be copied into this cell. 

# In[ ]:


# Step 2: Write code here


# In[2]:


import requests
import pandas


url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

querystring = {"type":"get-movies-by-title","title":"cheaper by the dozen"}

headers = {
    'x-rapidapi-key': "d6d20869a4msh34cebacbb5ab704p1ec73fjsnf5efc35efba9",
    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

import json 

r = requests.get('https://movies-tvshows-data-imdb.p.rapidapi.com/')
x = r.json()
df = pd.read_json

def GetMovieInfo():
    response = requests.get('https://movies-tvshows-data-imdb.p.rapidapi.com/')
    data_dict = response.json()
    activity = data_dict
    return activity
GetMovieInfo()


# ### No Grading at This Point, Only feedback
# 
# Remember you will not recieve a grade for P2, only feedback to get you to the next phase. Late or incomplete submissions will affect your grade. Consult the syllabus.
# 
# When you are ready, turn in your P2 using the submission script.

# In[ ]:


# run this code to turn in your work!
from coursetools.submission import Submission
Submission().submit()

