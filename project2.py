##### New Code generatiing from a free News API #####

##### Haiku Group 15 Discord-bot #####

#%%

import requests
import random
import syllapy


# This Code generates a Haiku from the news headlines and sends it to a Discord channel using a webhook.
### The API is NewsAPI.org and it is free to use. ###

API_KEY = 'Your API key here' ### This key is provided by NewsAPI.org (obtained upon registering on the website)


url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}' ### this is the link to which we will generate the Haikus from they're Headlines####


DISCORD_WEBHOOK_URL = 'insert your discord link here' ## Discord server link this current link is a test link ##



def count_syllables(word):
    return syllapy.count(word)

### Fuction to create the Haiku using the headlines and make them syllabes 5-7-5 ###
def create_haiku(headlines):
    haiku = []
    words = headlines.split()
    syllables_target = [5, 7, 5]
    
    
    if len(words) < 5:
        return "Not enough words to create a haiku."
    
    
    line_1 = ' '.join(words[:5])
    
    
    line_2 = ' '.join(words[5:12])
    
    
    line_3 = ' '.join(words[12:17])
    
    return f"{line_1}\n{line_2}\n{line_3}"


response = requests.get(url)


if response.status_code == 200:
   
    data = response.json()

    
    articles = data['articles'][:1]

    
    for article in articles:
        title = article['title']
        description = article['description'] or ""
        
        
        haiku_text = title if len(title.split()) > 5 else description
        
        
        haiku = create_haiku(haiku_text)

        
        print(f"{article['title']}")
        print(haiku)

        
        payload = {
            "content": f"{article['title']}\n{haiku}"
        }

        
        requests.post(DISCORD_WEBHOOK_URL, json=payload)

print('brought to you by Group 15')
# %%
