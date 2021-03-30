import re

import requests
from bs4 import BeautifulSoup
import io
import re
import praw
import re
from nltk.corpus import stopwords, brown
from nltk.tokenize import word_tokenize
import spacy

def cleanComment1(comment):
    data = re.sub('http\S+|www\S+', '', comment)
    data = re.sub('Attached Files|Click aici', '', data)
    data = re.sub('\S+.jpg|\S+.png|\S+K|\w+.jpg|\w+.png|\w+K', '', data)
    data = re.sub('\d{2} \w+ \d{4} \- \d{2}\:\d{2}', '', data)
    data = re.sub('Edited | Edited on |by \w+\, | downloads|said| said| said| on ', '', data)
    data = re.sub('\:| \, |\[|\]| \- |\,\,|\)\)', '', data)
    data = re.sub('  ', '', data)
    data = re.sub('\(embed\)', '', data)
    return data

def cleanComment2(comment):
    result = list()
    englishWords = set(w.lower() for w in brown.words())
    for comment in comment:
        tokens = word_tokenize(comment)
        comm = str()
        for word in tokens:
            if word not in englishWords:
                if word.isalpha():
                    comm+=word+" "
        result.append(comm)
    return result


if __name__ == '__main__':
    links_forum_softpedia = [
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__18",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__36",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__54",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__72",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__90",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__108",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__126",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__144",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__162",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__198",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__216",
        "https://forum.softpedia.com/topic/1165051-arta-moderna-reducerea-la-esenta-sau-lene/page__st__234",
        "https://forum.softpedia.com/topic/1101427-atat-rationamentul-cat-si-adevarul-sunt-falsificari-pragmatice-referitor-la-realitate/",
        "https://forum.softpedia.com/topic/1101427-atat-rationamentul-cat-si-adevarul-sunt-falsificari-pragmatice-referitor-la-realitate/page__st__18",
        "https://forum.softpedia.com/topic/1187056-olarit/"]

    comments=[]

    for link in links_forum_softpedia:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(z_itemprop="commentText")
        for result in soup.select('[z_itemprop="commentText"]'):
            comments.append(result.get_text("\n", strip=True))
            # print(result.get_text("\n", strip=True))
    with open("../CommentsColected/softpedia.txt", "w+", encoding="utf-8") as f:
        for comment in comments:
            f.write("ANNOTATION\n")
            data=cleanComment1(comment)
            f.write(data)
            f.write("\n")
    f.close()
    print("Done")


