#import requests

#r = requests.get('https://httpbin.org/')
#print(r.encoding)

#for line in r.iter_lines():
    #print(line)


from jikanpy import Jikan
jikan = Jikan()

anime = jikan.anime(52991, extension='episodes')
for episode in anime['data']:
    print(f"Епізод №{episode['mal_id']} з назвою: {episode['title']} має рейтинг {episode['score']}")