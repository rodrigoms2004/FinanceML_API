import os
from flask import Flask, jsonify, request
from textblob import TextBlob
from sentimentAnalysis import sentimentValueFromTweeter

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

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


@app.route('/api/sentimentValue', methods=['POST'])
def sentimentValue():
    tweets = request.get_json()
    
    sValue = sentimentValueFromTweeter(tweets)

    return jsonify({ "success": True, "sentimentValue": sValue })


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)


# python src/app.py

# FLASK_APP=app.py flask run