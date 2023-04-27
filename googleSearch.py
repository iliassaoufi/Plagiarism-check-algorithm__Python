from bs4 import BeautifulSoup
from requests import get

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/61.0.3163.100 Safari/537.36'
})


def search_content(query, type=1):
    language_code = "fr"
    search_term = query.replace(' ', '+')
    if type != 2:
        search_term = '"'+search_term+'"'

    google_url = 'https://www.google.com/search?q={}&hl={}&num=15&oq=go&aqs=edge.1.69i60j0i131i433i512l2j69i57j69i59j69i60l4.2070j0j1&sourceid=chrome&ie=UTF-8'.format(
        search_term,   language_code)

    response = get(google_url, headers=HEADERS)

    src = response.content
    soup = BeautifulSoup(src, 'html.parser')

    content_array = soup.get_text().split("secondes)")[
        1].split("Web")[1:]
    content = ' web '.join(content_array)

    return content


# HEADERS_all = ({
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Referer": "https://www.google.com/",
#     "Sec-Ch-Ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"92\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
#     "X-Amzn-Trace-Id": "Root=1-6119c652-54b9df497ac083bd73adffdc",
# })


# text = "La dernière partie est visiteur est une personne qui ne possèdent pas de compte et n'a pas un large"
# print(search_content(text))
