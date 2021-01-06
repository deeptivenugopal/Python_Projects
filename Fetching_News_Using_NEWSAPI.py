# importing requests package 
import requests,json

def NewsFromBBC():

    # BBC news api
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=f4c122de2c204ee68d221edeba7aec97"

    # fetching data in json format
    open_bbc_page = requests.get(main_url)
    

    #get response in json format
    open_bbc_page_resp = open_bbc_page.json()
    #print(open_bbc_page_resp)

    # getting all articles in a list
    article = open_bbc_page_resp['articles']
    #print(type(article))
    #print(article)

    # empty list which will  
    # contain all trending news
    results = []

    #append news articles in results
    for ar in article:
        print(ar)
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i+1,results[i])

    #to read the news out loud for us
    '''import win32com.client 
    speak = win32com.client.Dispatch("SAPI.Spvoice")
    speak.Speak(results)'''

#calling the news method                  
NewsFromBBC()
