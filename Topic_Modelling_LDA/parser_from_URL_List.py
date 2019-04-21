# -*- coding: utf-8 -*-
#from warcio.archiveiterator import ArchiveIterator
URL_list=[]
nytimes="nytimes"
with open('march14', 'r') as stream:
	#a=stream.readline();
	URL_list=stream.readlines();
#print(URL_list)
import requests
final_dict={}
for each in URL_list:
    try:
        page = requests.get(each)
        data=page.text
        from bs4 import BeautifulSoup as bs
        soup=bs(data,'html.parser')
        results=soup.findAll("title")
        headline=results[0].text.encode('ascii', 'ignore')
        article_body_tag=soup.find("section",{"name":"articleBody"})
        paragraph_tags=article_body_tag.findAll("p")
        paragraph_text=""
        for each in  paragraph_tags:
            paragraph_text+=each.text.encode('ascii', 'ignore')
            
            #paragraph_text+=new_line    
        final_dict[headline]=paragraph_text
    except:
        continue    
print(final_dict)    
