import googlesearch

query = "geeksforgeeks"

#Generator Object
res = googlesearch.search(query,stop=10)

for url in res:
    print(url)
