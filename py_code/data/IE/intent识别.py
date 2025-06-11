
import json

intent_lib = {
    "intents": {
        "souvenir_search": [
            "Find souvenirs by category",
            "Find souvenirs by brand",
            "Find souvenirs by flavor",
            "Find souvenirs by purchase location",
            "Find souvenirs by characteristics"
        ],
        "recommendation_requests": [
            "Get recommended souvenirs",
            "Get recommended brands",
            "Get recommended flavors",
            "Get purchase locations",
            "Get special notes"
        ]
    }
}

intents=[]
types=[]

for intent, exps in intent_lib['intents'].items():
    for exp in exps: 
        intents.append(intent)
        types.append(exp)

print(intents)
print(types)


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(types)

print(vectorizer.get_feature_names_out())

from sklearn.linear_model import LogisticRegression

#classifier = clf 分类器
clf = LogisticRegression()
clf.fit(X, intents)

nsentence = ["Find souvenirs by type"]
nX = vectorizer.transform(nsentence)
predict_intent = clf.predict(nX)
print(predict_intent)








