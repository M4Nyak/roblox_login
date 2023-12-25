import requests
from bs4 import BeautifulSoup
import re
def csrf_al():

 headers = {
    'authority': 'www.roblox.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.roblox.com/login',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

 response = requests.get('https://www.roblox.com/home',  headers=headers).text
 soup= BeautifulSoup(response,"html.parser")
 csrf = soup.find_all("meta",{"name": "csrf-token"})
 csrf_t= re.findall('n="\S+"',str(csrf))
 session_id = str(csrf_t[0]).strip('n=""')
 return session_id

def login():
 cookies = {
    '__utma': '210924205.8540409125.1679684617.1697825461.1698477145.92',
    '__utmz': '202924205.1692623377.38.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga': 'GA1.1.4188177230.1621889928',
    '_ga_BK4ZY0C59K': 'GS1.1.1193364277.2.1.1693230292.0.0.0',
    '_gcl_au': '1.1.1441391257.2596673046',
    'GuestData': 'UserID=-2329292428',
    'RBXSource': 'rbx_acquisition_time=12/24/2023 3:56:37 AM&rbx_acquisition_referrer=&rbx_medium=Direct&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1',
    'RBXEventTrackerV2': 'CreateDate=12/24/2023 10:30:12 AM&rbxid=3217369016&browserid=166785499812',
    'rbx-ip2': '',
}

 headerss = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'pragma': 'no-cache',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': csrf_al(),
}

 json_data = {
    'ctype': 'Username',
    'cvalue': 'Turkishboy_14',
    'password': 'KasparNico12123',
}

 response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headerss, json=json_data)
 return response.json()
print(login())
