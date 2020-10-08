
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup
import os
import urllib.parse


app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()



@app.route('/')
def home():
    quote = get_fact().strip()
    payload = {'input_text': quote}
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", payload)
    #logging.debug("Try get response url is{}:".format(response.url))
    #body = response.url
    body = '<a href= {}> {} </a>'.format(response.url, response.url)
    return Response(response=body, mimetype="text/html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6788))
    app.run(host='0.0.0.0', port=port)

