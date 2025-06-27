#!/usr/bin/env python
# coding: utf-8

# ### Combine trained models into one class

# In[35]:


import json
import re
import joblib
import pandas as pd
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tqdm.auto import tqdm
from sklearn.metrics import classification_report


# In[36]:


class Interpreter:
    def __init__(self,
                 intent_classifier=joblib.load("data/trained_model/intent_classifier.joblib"),
                 entity_recognizer=spacy.load("data/trained_model/entity_recognizer"),
                 IE_lib=json.load(open("data/IE/IE_lib.json",encoding="utf-8"))):
        self.intent_classifier=intent_classifier
        self.entity_recognizer=entity_recognizer
        self.sentiment_analyzer=SentimentIntensityAnalyzer()
        self.IE_lib=IE_lib

    def sentence_split(self,query):
        sentences = re.split(r'[.!?]+', query)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def interpret(self,user_input):
        sentence_set=self.sentence_split(user_input)
        def process_query(query):
            intent_pred=self.intent_classifier.predict([query])
            intent_name=intent_pred[0]
            entities_pred={
                ent.text:ent.label_ for ent in self.entity_recognizer(query).ents
            }
            sentiment_score=self.sentiment_analyzer.polarity_scores(query)
            result={
                "query":query,
                "intent":intent_name,
                "entities":entities_pred,
                "sentiment":sentiment_score
            }
            return result
        return [process_query(sentence) for sentence in sentence_set]


# In[37]:





# In[41]:

if __name__ == "__main__":

    interpreter=Interpreter()

    test_texts = [
        "Where is KK convenience store located?",
        "Can I go to A3 library tomorrow morning?",
        "What time does Starbucks open?",
        "Can I book a room in B1 Activity Building?"
    ]

    for text in test_texts:
        result=interpreter.interpret(text)
        # print(result)
        print(f"Query: {result[0]['query']}")
        print(f"Intent: {result[0]['intent']}")
        print(f"Entities: {result[0]['entities']}")
        print(f"Sentiment: {result[0]['sentiment']}")
        print("-"*40)


# In[ ]:




