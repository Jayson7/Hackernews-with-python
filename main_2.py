import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

print(len(r.json())) # 500
r.json()[0:100]

article_ids = r.json() # author used submission as variable name, but articles made more sense to me
five_articles_dicts = [] # this dict will contain all of our articles

for article_id in article_ids[:100]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(article_id) + '.json' # plug in looped id
    article_r = requests.get(url) # get response for each individual article

    #author prints out article status code to ensure no failures with requests
    print(article_r.status_code)

    one_article = article_r.json()

    # Now let's add our info to our main dictionary

    five_articles_dict = {
        'Title': one_article['title'],
        'Discussion link': one_article['url'],
        'Comments': one_article['descendants']
    }

    five_articles_dicts.append(five_articles_dict)

five_articles_dicts