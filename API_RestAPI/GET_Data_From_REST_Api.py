'''
How To Get Data From REST API With Python
https://www.codingthesmartway.com/how-to-get-data-from-rest-api-with-python/
For the following example we’ll use a REST service which is provided by JSONPlaceholder and can be found at https://jsonplaceholder.typicode.com/:
The specific endpoint which we’re using here is the /todos endpoint which is delivering a JSON list of todo items. The complete URL of this endpoint is https://jsonplaceholder.typicode.com/todos. This url is passed as a string argument to the call of requests.get. The result is stored in variable api_response.
'''

import requests
import json

api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(api_response.status_code)
data = api_response.text
parse_json = json.loads(data)

print("Todos:", parse_json)

'''
OUTPUT

200
Todos: [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}, {'userId': 1, 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum', 'completed': False}, {'userId': 1, 'id': 6, 'title': 'qui ullam ratione quibusdam voluptatem quia omnis', 'completed': False}, {'userId': 1, 'id': 7, 'title': 'illo expedita consequatur quia in', 'completed': False}, {'userId': 1, 'id': 8, 'title': 'quo adipisci enim quam ut ab', 'completed': True}, {'userId': 1, 'id': 9, 'title': 'molestiae perspiciatis ipsa', 'completed': False}, {'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True}, {'userId': 1, 'id': 11, 'title': 'vero rerum temporibus dolor', 'completed': True}, {'userId': 1, 'id': 12, 'title': 'ipsa repellendus fugit nisi', 'completed': True}, {'userId': 1, 'id': 13, 'title': 'et doloremque nulla', 'completed': False}, {'userId': 1, 'id': 14, 'title': 'repellendus sunt dolores architecto voluptatum', 'completed': True}, {'userId': 1, 'id': 15, 'title': 'ab voluptatum amet voluptas', 'completed': True}, {'userId': 1, 'id': 16, 'title': 'accusamus eos facilis sint et aut voluptatem', 'completed': True}, {'userId': 1, 'id': 17, 'title': 'quo laboriosam deleniti aut qui', 'completed': True}, {'userId': 1, 'id': 18, 'title': 'dolorum est consequatur ea mollitia in culpa', 'completed': False}, {'userId': 1, 'id': 19, 'title': 'molestiae ipsa aut voluptatibus pariatur dolor nihil', 'completed': True}, {'userId': 1, 'id': 20, 'title': 'ullam nobis libero sapiente ad optio sint', 'completed': True}, {'userId': 2, 'id': 21, 'title': 'suscipit repellat esse quibusdam voluptatem incidunt', 'completed': False}, {'userId': 2, 'id': 22, 'title': 'distinctio vitae autem nihil ut molestias quo', 'completed': True}, {'userId': 2, 'id': 23, 'title': 'et itaque necessitatibus maxime molestiae qui quas velit', 'completed': False}, {'userId': 2, 'id': 24, 'title': 'adipisci non ad dicta qui amet quaerat doloribus ea', 'completed': False}, {'userId': 2, 'id': 25, 'title': 'voluptas quo tenetur perspiciatis explicabo natus', 'completed': True}, {'userId': 2, 'id': 26, 'title': 'aliquam aut quasi', 'completed': True}, {'userId': 2, 'id': 27, 'title': 'veritatis pariatur delectus', 'completed': True}, {'userId': 2, 'id': 28,
'''