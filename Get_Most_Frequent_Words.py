# Python3 program for a word frequency 
# counter after crawling a web-page
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

'''Function defining the web-crawler/core 
spider, which will fetch information from 
a given website, and push the contents to 
the second  function clean_wordlist()'''
def start(url):

    # empty list to store the contents of  
    # the website fetched from our web-crawler
    wordList = []    
    sourceCode = requests.get(url).text

    # BeautifulSoup object which will 
    # ping the requested url for data
    soup = BeautifulSoup(sourceCode,'html.parser')

    # Text in given web-page is stored under 
    # the <div> tags with class <entry-content> entry-content
    for each_text in soup.findAll('div',{'class':'section'}):
        content = each_text.text
        
    # use split() to break the sentence into  
    # words and convert them into lowercase
    words = content.lower().split()

    for each_word in words:
        wordList.append(each_word)
    
    clean_wordlist(wordList)

# Function removes any unwanted symbols
def clean_wordlist(wordList):

    clean_list = []

    for word in wordList:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],'')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

def create_dictionary(clean_list):

    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
             word_count[word] = 1
    c = Counter(word_count)

    # returns the most occurring elements 
    top = c.most_common(10)
    print(top)

''' To get count of each word in 
        the crawled page --> 
          
    # operator.itemgetter() takes one  
    # parameter either 1(denotes keys) 
    # or 0 (denotes corresponding values) 
      
    for key, value in sorted(word_count.items(), 
                    key = operator.itemgetter(1)): 
        print ("% s : % s " % (key, value)) 
          
    <-- '''    

# Driver code
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/programming-language-choose/") #class = entry-content
    #start("https://www.geeksforgeeks.org/") #not able to figure out
    start("https://www.crummy.com/software/BeautifulSoup/bs4/doc/") # class = section
