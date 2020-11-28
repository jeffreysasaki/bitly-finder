import requests
import random
from flask import Flask, request

app = Flask(__name__)

def generate_base62_key():
  combination = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  key = str(random.randrange(1, 4))
  for n in range(6):
    key += combination[random.randrange(0, len(combination))]
  return key

def get_bitly_url(count):
  index = 0
  arr = []
  while index < count:
    test_url = 'https://bit.ly/' + generate_base62_key()
    try:
      req = requests.get(test_url)
      if req.status_code == 403:
        return ['You are currently shadow banned. Please try again later.']
      elif req.status_code == 200:
        arr.append(test_url)
        print(test_url)
        index += 1
    except:
      continue
  return arr

@app.route('/')
def index():
  count = int(request.args.get('count', '5'))
  result = ''
  for url in get_bitly_url(count): 
    result += '<h1><a href="' + url + '" target="_blank">' + url + '</a></h1>'
  return result
