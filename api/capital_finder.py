from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    list_of_dif=[]
    message="testing"
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)

    # print(111,my_dict)
    if 'capital' in my_dict:
      capital = my_dict.get('capital')
      url= f'https://restcountries.com/v3.1/capital/{capital}'
      res = requests.get(url+capital)
      data = res.json()
    #   print(222,data)
    for word_data in data :
      definition = word_data['name']["common"]
      message = str(f"{capital} is the capital of {definition}")
      list_of_dif.append(message)
    self.wfile.write(message.encode())
    return