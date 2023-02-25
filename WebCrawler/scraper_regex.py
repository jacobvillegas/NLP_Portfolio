# this is to be selective at the sites
import re
import urllib.parse

import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

URL = 'https://www.businessinsider.com/how-to-use-chatgpt-at-work-job-save-time-ai-2023-2?amp'
domain_name = urllib.parse.urlparse(URL)
print('StartDomain:', domain_name.netloc)
# print(type(domain_name.netloc))
start_page = requests.get(URL)
soup = BeautifulSoup(start_page.content, 'html.parser')


# used to obtain the embedded links within a site
def get_embedded_links(soupobj):
    out_url = []
    for para in soupobj.find_all('p'):
        for linky in para.find_all('a'):
            out_url.append(linky.get('href'))
    return out_url


out_going_links = get_embedded_links(soup)
print('Number of Outgoing Links:', len(out_going_links))
print(out_going_links[:5])
first_five = out_going_links[:5]


def filter_websites(websites, match_pattern):
    filtered_websites = []
    filtrate =[]
    pattern = re.compile(match_pattern)
    for website in websites:
        if not pattern.search(website):
            filtered_websites.append(website)
        else:
            filtrate.append(website)
    return filtered_websites, filtrate


# create a regex to limit sites with a certain domain name
domain_specific_regex = '(http|https):\/\/' + domain_name.netloc + '\/'
# print(type(domain_specific_regex))
print(domain_specific_regex)
chat_sites = '.com\/($chatgpt|chatgpt|-chat-gpt|-ai|-artificial-intelligence)'
regex_twit_tok_tube = '(http|https):\/\/www.(?!(twitter|youtube|tiktok|facebook|oecd-ilibrary))'
remove_pdf = '(.pdf|)$'


# used to get only two embedded website that share the same domain name
def get_two(websites, pattern):
    filter, leftover = filter_websites(websites, pattern)
    return filter[:2]


only_two = get_two(first_five, domain_specific_regex)
print(only_two)

social_media, not_social_media = filter_websites(out_going_links, regex_twit_tok_tube)
print(len(not_social_media))


other, otherx = filter_websites(not_social_media, domain_specific_regex)

for items in other:
    print(items)

two_sties = otherx[:2]
new_additions = otherx.pop()
other.append(new_additions)
print(other,len(other))
