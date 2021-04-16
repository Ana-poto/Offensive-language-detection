import requests
from bs4 import BeautifulSoup
allLink=[]
def getComments(URL):
    with requests.Session() as session:
        page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find_all(class_="comment-content")
    comments = []

    for coment in content:
        comments.append(coment.text)

    f = open("E:/GitHub/Offensive-language-detection/DataColector/ColectingPhase2/bzi.txt", "a", encoding="utf-8")
    for com in comments:
        f.write("ANNOTATION\n")
        f.write(str(com))
    f.close()

def getLink(URL):
    print(str(len(allLink))+"t")
    with requests.Session() as session:
        page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    find_all_a = soup.find_all("a", href=True)

    print(len(find_all_a))
    for el in range(27, int(len(find_all_a)/1.2), 2):

        if ("https://www.bzi.ro/" in find_all_a[el]['href'] and "whatsapp://send?text=" not in find_all_a[el]['href'] and "https://www.bzi.ro/poze/" not in find_all_a[el]['href'] and "https://pinterest.com" not in find_all_a[el]['href'] and "https://www.facebook.com/sharer" not in find_all_a[el]['href']):
            if(find_all_a[el]['href'] not in allLink):
                allLink.append(find_all_a[el]['href'])
                getComments(find_all_a[el]['href'])
                print(find_all_a[el]['href'])


getComments("https://www.bzi.ro/el-este-tanarul-care-a-murit-la-volanul-bmw-ului-izbit-de-tren-era-student-la-iasi-exclusiv-4128203?utm_source=website&utm_medium=top-stiri")
getComments("https://www.bzi.ro/campanie-de-donatii-pentru-inmormantarea-tinerilor-ucisi-in-gravul-accident-feroviar-din-iasi-4128578?utm_source=website&utm_medium=top-stiri")
getComments("https://www.bzi.ro/cea-mai-sexy-cantareata-din-iasi-era-sa-si-piarda-viata-in-bucium-dupa-ce-a-provocat-un-accident-spectaculos-tanara-s-a-laudat-peste-tot-cu-bmw-ul-ei-de-zeci-de-mii-de-euro-pe-care-l-a-facut-praf-4133630?utm_source=website&utm_medium=top-stiri")
getComments("https://www.bzi.ro/imagini-cu-un-puternic-impact-emotional-momentul-accidentului-mortal-in-care-un-bmw-a-fost-izbit-in-plin-de-tren-a-fost-filmat-ce-a-facut-soferul-in-ultima-clipa-de-viata-video-4130192?utm_source=website&utm_medium=top-stiri")
getComments("https://www.bzi.ro/imaginile-care-fac-inconjurul-tarii-un-primar-din-iasi-este-batut-cu-bestialitate-chiar-in-mijlocul-comunei-pe-care-o-conduce-de-o-gasca-de-derbedei-s-a-lasat-cu-dosar-penal-si-cu-arestari-in-weeken-4137192?utm_source=website&utm_medium=top-stiri")
getComments("https://www.bzi.ro/accident-feroviar-grav-in-iasi-doua-persoane-si-au-pierdut-viata-4128139?utm_source=website&utm_medium=top-stiri")

with requests.Session() as session:
    page = requests.get("https://www.bzi.ro/")

soup=BeautifulSoup(page.content,"html.parser")
find_all_a = soup.find_all("a", href=True)

print(len(find_all_a))
for el in range(27,int(len(find_all_a)/1.2),2):

    if("http" in find_all_a[el]['href']):
        print(find_all_a[el]['href'])
        getComments(find_all_a[el]['href'])
        getLink(find_all_a[el]['href'])



