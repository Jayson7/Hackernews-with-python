import requests 
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json' # to obtain list of top story ids
r = requests.get(url)

article_ids = r.json() # author used submission as variable name, but articles made more sense to me
five_articles_dicts = [] # this dict will contain all of our articles

for article_id in article_ids[:100]: # we only want the first 100 articles
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(article_id) + '.json' # plug in looped id
    article_r = requests.get(url) # get response for each individual article

    #author prints out article status code to ensure no failures with requests
    # print(article_r.status_code)

    one_article = article_r.json()
    # print(one_article)
    # Now let's add our info to our main dictionary

    five_articles_dict = {
        'Title': one_article["title"],
        'Type': one_article["type"],
        'Author': one_article["by"],
        'Score': one_article["score"],
        'Time': one_article["time"],
        

    }
    

    if 'url' in one_article:
        five_articles_dict['Discussion link'] = one_article["url"],
    else:
        five_articles_dict['Discussion link'] = 'No discussion link',

    if 'descendants' in one_article:
        five_articles_dict['Comments'] = one_article["descendants"],
    else:
        five_articles_dict['Comments'] = 'No comments',
        
        
    five_articles_dicts.append(five_articles_dict)

# print(five_articles_dicts)

# sorted_dict = sorted(five_articles_dicts, key=itemgetter('Comments'), reverse=True) #'True' for highest to lowest
# print(sorted_dict)

for article in five_articles_dicts:
    print('\nTitle:', five_articles_dicts['Title']) # \n to add a break between each five_articles_dicts's info
    print('Discussion Link:', five_articles_dicts['Discussion link'])
    print('Comments:', five_articles_dicts['Comments'])