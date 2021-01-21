#Web Scraping
"""This is a mini web scraping project done for educational purpose. 
The URL is of a blogger named Harry, who has allowed people to do scraping on his website. 
I collected two main information from his page i.e 
blog title and its respective few lines of description for multiple pages. 
I have stored the data using SQL programming language by performing various 
operations on the database
"""

import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import sql


parser= argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the no. of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter name of the db ", type=str)
args=parser.parse_args()

# Getting HTML
url="https://www.codewithharry.com/blog/?number="

page_num_MAX=args.page_num_max
scrapped_info_list=[]

sql.connect(args.dbname)  
for page_num in range(1, (page_num_MAX+1)):
    url1=url+str(page_num)
    print("GET request for: " + url1)
    req=requests.get(url1)
    htmlcontent=req.content
    #print(htmlcontent)
    
    #Parsing 
    soup=BeautifulSoup(htmlcontent,'html.parser')
    #print(soup)
    
    #HTML tree trasversal
    #Finding all the blogs title
    blog_title=soup.find_all('h2')
    #print(blog_title) #This will result in HTML code
    #print(soup.find('h2').text) #This will extract all the titles from HTML code
    
    #Extracting blog paragraphs
    blog_para=soup.find_all('p')
    
    #Finding individual blog titles
    #for num in blog_title:
    for count,num in enumerate(blog_title,0):
        for count1,num1 in enumerate(blog_para,0):
        #for num1 in blog_para:
            if count==count1:
                #paragraphs of blog titles
                if blog_para.index(num1)==len(blog_title):
                    break
                else:
                    #print(num1.text)    
                    dict={}
                    dict["TITLE"]=num.text
                    dict["DESCRIPTION"]=num1.text
                    #print(num.text)
                    scrapped_info_list.append(dict)
                    sql.insert_into_table(args.dbname, tuple(dict.values()))

            
#Storing data in csv file
dataFrame=pandas.DataFrame(scrapped_info_list)
#print('Creating a CSV file ...')
dataFrame.to_csv("Blogpost4.csv")

#Storing data in database
print('\nData base is as follows:\n')
sql.get_blog_info(args.dbname)

