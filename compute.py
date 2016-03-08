# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def compute(something):
  links = []
  r = requests.get(something)
  soup = BeautifulSoup(r.text)
  for a in soup.find_all('a', href=True):
    links.append(a['href'])
    #soup.getText()
  return links
