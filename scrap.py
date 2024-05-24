import requests
import json
from bs4 import BeautifulSoup
from leetcode_scraper import LeetcodeScraper

scraper = LeetcodeScraper()

def codf(url):
    response = requests.get('https://codeforces.com/profile/'+url)
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.select('div._UserActivityFrame_counterValue')[0].text.split()[0]
    return res
# print(codf('https://codeforces.com/profile/eyobworku'))

def letco(user):
    profile_data = scraper.scrape_user_profile(user)
    da = profile_data['userProblemsSolved']['matchedUser']['submitStatsGlobal']['acSubmissionNum']
    t,e,m,h = da[0]['count'],da[1]['count'],da[2]['count'],da[3]['count']
    return t

# f = open("letuser.txt", "r")
# for x in f:
#     print(codf(x.strip()))
# f.close()
