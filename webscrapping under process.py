# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:15:00 2020

@author: Dattu
"""
#importing packages
from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup

#web page details
my_url = 'https://www.newegg.com/p/pl?d=graphics+card'
uClient = Ureq(my_url)

#reading web pags 
page_raw_html = uClient.read()
uClient.close()

#parsing web pages to html pages
page_soup = soup(page_raw_html, "html.parser")
#print(page_soup.h1)
#print(page_soup.h2)
#print(page_soup.body)
containers = page_soup.findAll('div',{"class":"item-container"})
print(containers)