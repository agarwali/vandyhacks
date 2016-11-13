import json
from watson_developer_cloud import AlchemyLanguageV1 as alchem
from google import search

class SentimentAnalyzer:
    def __init__(self, key):
        self.key = key
        self.alchem = alchem(api_key = self.key)
    
    def get_sentiment(self, keywords, urls):
        sentiment = 0
        count = 0
        for url in urls:
            try:
                res = self.alchem.targeted_sentiment(url=url,targets=keywords)
                count +=1
            except Exception, e:
                print e
            sentiment += float(res['results'][0]['sentiment']['score'])
            print count
        if count == 0:
            return -1
        return (sentiment/count)

    def get_urls(self, searchString):
        return search(searchString, lang='es', stop=10)
        

def main():
    watson = SentimentAnalyzer('b3ab2920d3b2a7215389dddeec54bf1ed0724ae1')
    urls = watson.get_urls('bernie sanders abortion')
    keywords = ["abortion"]
    print watson.get_sentiment(keywords, urls)


if __name__ == "__main__":
    main()
