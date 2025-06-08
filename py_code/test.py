from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
test=input("You:")
while test!="quit":
    print("Result:",SentimentIntensityAnalyzer().polarity_scores(test))
    test=input("You:")