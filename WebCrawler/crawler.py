from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.error import HTTPError
from website_regex import *
from text_processing import create_txt_file


class Crawler:
    def __init__(self, url):
        self.url = url
        self.buffer = []
        self.sites_visited = []
        self.counter = 15

    def start_request(self):
        return urlopen(self.url).read().decode('utf-8-sig')

    def external_request(self, embedded_links):
        return urlopen(embedded_links).read().decode('utf-8-sig')

    def get_embedded_links(self, soup_obj):
        out_url = []
        for paragraphs in soup_obj.find_all('p'):
            for embed_links in paragraphs.find_all('a'):
                out_url.append(embed_links.get('href'))
        return out_url

    def added_to_visited(self, website):
        self.sites_visited.append(website)

    def add_to_buffer(self, list_websites):
        for site in list_websites:
            self.buffer.append(site)

    def get_text(self, request):
        raw_text = BeautifulSoup(request, "html.parser", parse_only=SoupStrainer('p')).get_text()
        return raw_text

    def crawl_pipline(self, request, website, soup_object):
        # ----add website to buffer, and traversed lists----
        self.added_to_visited(website)
        print(self.counter)
        # -----Use Soup Object to get all embedded links--
        external_sites = self.get_embedded_links(soup_object)
        print('EXTERNAL:', external_sites)
        # ---use Regex to fileter out social media sites, then the sites that have the same domain name.---
        social_media, no_social_media = filter_websites(external_sites, regex_twit_tok_tube)
        # print('reduced sites-no media', no_social_media)
        no_pdf_sites, pdf_sites = filter_websites(no_social_media, regex_pdf)
        # -------------------(end of regex filter)-----------------------------------------
        # add filtered external links to buffer
        self.add_to_buffer(no_pdf_sites)
        print('Current Buffer:', self.buffer)
        # ------ get the text ----
        web_text = self.get_text(request)
        print(web_text)
        # -------- Create Text Files ----------------------------------------------
        create_txt_file(web_text, self.counter)
        # return no_social_media

    def start_up(self):
        start_site = urlopen(self.url).read().decode('utf-8-sig')
        soup = BeautifulSoup(start_site, 'html.parser')
        self.crawl_pipline(start_site,self.url, soup)


    def crawl(self):
        self.start_up()
        link_from_buffer = self.buffer.pop(0)
        print('Popped Site', link_from_buffer)
        print('New Buffer:', self.buffer)
        print('Starting buffer Length:', len(self.buffer))
        while self.counter > 0:
            # ---- second round----
            if link_from_buffer not in self.sites_visited:
                try:
                    site_request = urlopen(link_from_buffer).read().decode('utf-8-sig')
                except HTTPError as e:
                    print('HTTP ERROR - skipping', e)
                    #self.counter -= 1
                else:
                    self.counter -= 1
                    new_soup = BeautifulSoup(site_request, 'html.parser')
                    next_iteration = self.crawl_pipline(site_request, link_from_buffer, new_soup)
                    print("new links:", next_iteration)
                    print("next iter buffer", self.buffer)
                    print("Current Size of Buffer", len(self.buffer))
            else:
                option = self.buffer.pop(0)
                try:
                    alt_site_request = urlopen(option).read().decode('utf-8-sig')
                except HTTPError as e:
                    print('HTTP ERROR - skipping', e)
                    #self.counter -= 1
                else:
                    self.counter -= 1
                    new_soup = BeautifulSoup(alt_site_request, 'html.parser')
                    alt_iteration = self.crawl_pipline(alt_site_request, option, new_soup)
                    print("Alt new links:", alt_iteration)
                    print("alter buffer", self.buffer)
                    print("Length of Buffer:", len(self.buffer))


URL = 'https://www.businessinsider.com/how-to-use-chatgpt-at-work-job-save-time-ai-2023-2?amp'

creepy_2 = Crawler(URL)
creepy_2.crawl()
