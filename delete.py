
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import logging

logging.basicConfig(level=logging.DEBUG)

payload = {'input_text': 'try this'}
response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", payload)
logging.debug("Try get response url is{}:".format(response.url))

print('hmmm')




