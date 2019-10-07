from flask import Flask,render_template,request,jsonify
from textblob import TextBlob
import json


with open('./src/config/config.json') as config:
    data = json.load(config)
    port = data['serverPort']

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    tweets = request.get_json()
    
    sentimentList = []
    
    for tweet in tweets:
      sentiment = {}
      polarity = TextBlob(tweet['text']).sentiment.polarity
      subjectivity = TextBlob(tweet['text']).sentiment.subjectivity

      sentiment['text'] = tweet['text']
      sentiment['polarity'] = polarity
      sentiment['subjectivity'] = subjectivity

      sentimentList.append(sentiment)
      
    return jsonify({ "success": True, "sentimentList": sentimentList })


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=port)


# python src/app.py


# @app.route('/api/<id>', methods = ['GET', 'POST', 'DELETE', 'PUT'])
# def api(id):
#   if request.method == 'GET':
#     return 'GET Method:' + id

#   if request.method == 'POST':
#     data = request.get_json()
#     print(data)
#     return 'JSON posted'

#   if request.method == 'DELETE':
#     return 'Deleted id:' + id

#   if request.method == 'PUT':
#     return 'Updated id:' + id

#   else:
#     return 'invalid'


