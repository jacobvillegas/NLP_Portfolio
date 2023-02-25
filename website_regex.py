
import re
import urllib.parse

# domain_name = urllib.parse.urlparse(URL)
# domain_specific_regex = '(http|https):\/\/' + domain_name.netloc + '\/'
regex_twit_tok_tube = '(http|https):\/\/www.(?!(twitter|youtube|tiktok|facebook|oecd-ilibrary))'
regex_pdf = '\.pdf?'


# Function to filter websites using regex pattern matching
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

