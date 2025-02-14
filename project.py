#### Project 1.3 Haiku Group 15 ######

#%%

import requests
from bs4 import BeautifulSoup

##### Scraping BBC News Headlines #####
def get_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')
    return [headline.get_text() for headline in headlines if headline.get_text()]

####### Generating Haiku #####

#%%

from nltk.corpus import cmudict

########## Load CMU Pronouncing Dictionary ####
pronouncing_dict = cmudict.dict()

def syllable_count(word):
    """Count syllables in a word using CMU dictionary"""
    word = word.lower()
    if word in pronouncing_dict:
        return max([len(list(y)) for y in pronouncing_dict[word]])
    else:
        return 1

def count_syllables_in_sentence(sentence):
    """Count total syllables in a sentence"""
    words = sentence.split()
    return sum(syllable_count(word) for word in words)

### Create Haiku from Headlines ###

#%%

def create_haiku(headlines):
    haiku = []
    syllables_target = [5, 7, 5]
    
    ##### Try to find sentences with 5, 7, and 5 syllables #####
    for target in syllables_target:
        for headline in headlines:
            if count_syllables_in_sentence(headline) == target:
                haiku.append(headline)
                headlines.remove(headline)
                break
    return "\n".join(haiku)

##### Post the Haiku to Discord ######
#%%

import requests

def post_to_discord(haiku, webhook_url):
    """Send the haiku to a Discord channel via webhook"""
    data = {
        "content": haiku
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Successfully posted haiku to Discord.")
    else:
        print("Failed to post to Discord:", response.status_code)


#### Main Script to Collect Data and Post Haiku ######

#%%

import random

def main():
    
    webhook_url = "https://discord.com/api/webhooks/1339505519643070526/GU0MOL-ueEZHYtBs1o7paf-BK-4L8O0HbkWMmCVR_zNNCanbU5QQYDPZIi2PyNlVzgJj"
    
    
    headlines = get_headlines()
    
    
    if len(headlines) >= 3:
        haiku = create_haiku(headlines)
        
        ##### Posting to Discord Web server #####
        post_to_discord(haiku, webhook_url)
    else:
        print("Not enough headlines to create a haiku.")

###### Code ends here ######