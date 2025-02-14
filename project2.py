##### New Code generatiing from a free News API #####

##### Haiku Group 15 Discord-bot #####

#%%

import requests
import random

# This Code generates a Haiku from the news headlines and sends it to a Discord channel using a webhook.
### The API is NewsAPI.org and it is free to use. ###

API_KEY = '1a1f87bf5bdd40cf94f092befe40804e'


url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'


DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1339505519643070526/GU0MOL-ueEZHYtBs1o7paf-BK-4L8O0HbkWMmCVR_zNNCanbU5QQYDPZIi2PyNlVzgJj'


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

    
    articles = data['articles'][:2]

    
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

# %%
