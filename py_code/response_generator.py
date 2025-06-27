#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from templates import match_template, Templates
import json


# In[6]:





# In[7]:


class ResponseGenerator:
    def __init__(self):
        self.database = json.load(open("data/extracted_json/database.json", "r", encoding="utf-8"))
        self.templates = Templates
    
    def search_info(self, interpreted_dict):
        intent = interpreted_dict["intent"]
        entity = list(interpreted_dict["entities"].keys())[0] # entities is a dictionary
        info_to_search = self.templates[intent]["info"]
        ans = {info: None for info in info_to_search}

        # Search for the entity in the database
        entity_info = None
        for category in self.database.keys():
            for item_main_key in list(self.database[category].keys())[1:]:
                #e This condition will be changed to a more general one
                if entity in self.database[category][item_main_key]['possible_name']:
                    entity_info = self.database[category][item_main_key]
                    break
            if entity_info:
                break
        for info in info_to_search:
            if info in entity_info.keys():
                ans[info] = entity_info[info]
        print("Info searched: \n", ans)
        return ans
    
    def sentiment_tagging(self, interpreted_dict):
        sentiment = interpreted_dict["sentiment"]
        if sentiment["compound"] > 0.05:
            return "positive"
        elif sentiment["compound"] < -0.05:
            return "negative"
        else:
            return "neutral"
    
    def generate_response(self, interpreted_dict):
        info = self.search_info(interpreted_dict)
        sentiment = self.sentiment_tagging(interpreted_dict)
        intent = interpreted_dict["intent"]
        return match_template(intent, sentiment, info)


# In[ ]:
if __name__ == "__main__":
    test_dict = {
        "intent": "ask_restaurant_recommendation",
        "entities": {"Starbucks": "restaurant_name"},
        "sentiment": {"compound": 0}
    }
    response_generator = ResponseGenerator()
    print(response_generator.generate_response(test_dict))




# %%
