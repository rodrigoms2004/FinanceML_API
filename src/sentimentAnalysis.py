import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def read_dict(data, name):

    # Internal  function. reacs a cictionary in the rows and makes a coulmn from a keyword
    arr = []
    length = int(data.shape[0])
    for i in range(length):
        arr.append(data['polarity'][i][name])
    data[name] = arr 
    return data

def sentimentValueFromTweeter(tweets):

  # Download lexicon
  nltk.download('vader_lexicon')


  # Creating a list of tweets
  tweets_text = list(map(lambda t: t['text'], tweets))
  
  # Tweets dataframe
  data = pd.DataFrame(data=tweets_text, columns=['Tweets'])

  # Sentiment analysis
  sia = SentimentIntensityAnalyzer()

  # Polarity
  sentimentList = []
  for index, row in data.iterrows():
    polarityScore = sia.polarity_scores(row["Tweets"])
    sentimentList.append(polarityScore)

  # Transform the list into a series
  sentimentSeries = pd.Series(sentimentList)

  # Create a new column in the dataframe
  data['polarity'] = sentimentSeries.values

  opnions = ['neg', 'neu', 'pos'] # negative, neutral, positive
  for option in opnions:
    data = read_dict(data, option)
  
  # Remove all 100% neutral
  filtered = data[data['neu'] != 1]

  # Spliting values
  result = filtered.sum(axis = 0)
  result.drop(['Tweets'], inplace=True)

  # Define the sentiment
  # if negative sentiment is three times bigger than positive sentiment
  if result['neg'] > 3*result['pos']:
      sentiment = -3

  # else if negative sentiment is twice bigger than positive sentiment
  elif result['neg'] > 2*result['pos']:
      sentiment = -2
      
  # else if negative sentiment is a bit bigger than positive sentiment
  elif result['neg'] > result['pos']:
      sentiment = -1

  # else if negative sentiment is three times smaller than positive sentiment
  elif 3*result['neg'] < result['pos']:
      sentiment = 3

  # else if negative sentiment is twice smaller than positive sentiment
  elif 2*result['neg'] < result['pos']:
      sentiment = 2

  # else if negative sentiment is a bit smaller than positive sentiment
  elif result['neg'] < result['pos']:
      sentiment = 1

  # else NOBODY CARES ABOUT YOUR KEYWORD
  else:
      sentiment = 0

  return sentiment # -3, -2, -1, 0, 1, 2, 3