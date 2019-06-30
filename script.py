import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://newsapi.org/v2/everything?q=bitcoin&from=2019-06-30&sortBy=publishedAt&apiKey=bc1119ab6a4c450fb7230c4c765ac97f') as info:

    res = info.read()
    decod = res.decode('utf-8')
    print(textwrap.fill(decod))
