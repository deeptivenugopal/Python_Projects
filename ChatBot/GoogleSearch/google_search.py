import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup


def chatbot_query(query,index=0):
	fallback ='Sorry, I cannot think of a reply for that.'
	result=''
	try:
		search_result_list = list(search(query,tld="co.in",num=10,stop=3,pause=1))
		#print("Search: ",search_result_list)
		
		page = requests.get(search_result_list[index])
		#print("Page: ",page)
		
		tree = html.fromstring(page.content)
		#print("Tree: ",tree)

		soup = BeautifulSoup(page.content,features="lxml")
		
		#print(soup)
		
		article_text=''
		article = soup.findAll('p')
		for element in article:
			article_text +='\n' +''.join(element.findAll(text=True))
		
		#print("Article Text: ",article_text)
		article_text = article_text.replace('\n','')
		
		first_sentence = article_text.split('.')
		first_sentence = first_sentence[0].split('?')[0]
		#print("first Sentence: ",first_sentence)
		
		chars_without_whitespace = first_sentence.translate(
            {ord(c):None for c in string.whitespace}
        )
		#print("chars: ",chars_without_whitespace)
		
		if len(chars_without_whitespace) > 0:
			result = first_sentence
			print("result: ",result)
		else:
			result = fallback
		#print("result: ",result)
		return result
	except:
		if len(result) == 0: result = fallback
		return result

#chatbot_query('Testing',index=0)
