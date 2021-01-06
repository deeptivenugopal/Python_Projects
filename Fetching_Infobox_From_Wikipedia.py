'''import requests
from lxml import etree

url="https://en.wikipedia.org/wiki/Delhi_Public_School_Society"

req = requests.get(url)
print(req.text)

store = etree.fromstring(req.text)

print(store.tag)'''
# importing modules 
import requests 
from lxml import etree 
  
# manually storing desired URL 
url='https://en.wikipedia.org/wiki/Delhi_Public_School_Society'
  
# fetching its url through requests module   
req = requests.get(url)  
  
store = etree.fromstring(req.text)

# this will give Motto portion of above  
# URL's info box of Wikipedia's page 
output = store.xpath('//table[@class="infobox vcard"]/tr[th/text()="Motto"]/td/i')  
  
# printing the text portion 
print(output[0].text) 
  
# Run this program on your installed Python or  
# on your local system using cmd or any IDE. 


