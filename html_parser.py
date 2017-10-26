#-*- coding: UTF-8 -*- 

'''
Created on 2017年10月25日

@author: 406
'''

from bs4 import BeautifulSoup
import re

class url_parser(object):

    def geturls(self, pageurl, soup):
        newurls = set()

        print 'pageurl' , pageurl
        links = soup.find_all('a', href = re.compile(r'/item/.*?'))

        for link in links:

            newurl = link['href']

            fullurl = 'https://baike.baidu.com' + newurl

            newurls.add(fullurl)
    
        return newurls

    def geturldata(self, pageurl, soup):
        
        newdata = {}
        
        #获取url
        newdata['url'] = pageurl
        
        #获取网页标题
        title = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        if title == None:
            return None
        newdata['title'] = title.get_text().strip()
        
        #获取网页摘要
        summary = soup.find('div', class_ = 'lemma-summary')
        
        if summary == None:
            return None
        newdata['summary'] = summary.get_text().strip()
        
        return newdata
    
    def parser_html(self, pageurl, page):
        if pageurl is None or page is None:
            return None
        
        soup = BeautifulSoup(page, 'html.parser', from_encoding= 'utf-8') 
        
        new_urls = self.geturls(pageurl, soup)
        new_data = self.geturldata(pageurl, soup)

        return new_data, new_urls

