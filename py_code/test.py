import os
import re
import json

from openai import OpenAI
api_key=os.getenv("DEEPSEEK-API")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

instruction='''You are an expert NLU data generation assistant for a campus chatbot.
Your task is to generate {num_query} varied data items for given entity and intent.
**Instructions:**
1. You should generate {num_query} possible queries corresponding to the given entity and intent.
2. The output should be a vaild json snippet like {example}
3. The {num_query} queries should be included in a list.
in json file that is "query":[{num_query} generated] 
4. Each possible query must contain one or some of the given entities.
5. Each possible query must contain one or some of the given intents.
6. You cannot add new eneities in the generated query! 
For example:
"entity":{"gym":"facility_name"}, "generated_query":"When does the gym open on weekends"
then a NEW entity "weekend":"time" is added.
7. Output json snippet ONLY. 

**Exapmle:**
{
  "query": ["where is Nasi Kandar restaurant?", "how can i go to Nasi Kandar restaurant?"],
  "intent": "find_location",
  "entities": [
    {"Nasi Kandar restaurant":"reataurant_name"} 
  ]
}
'''

class NLU_data_generator:
    def __init__(self,intent_lib_path=r"py_code\data\IE\intent_lib.json"):
        self.data=json.load(open(intent_lib_path,"r",encoding="utf-8"))
        self.categories=list(self.data.keys())
        self.responses={
          category:None for category in self.categories
        }
    
    def create_prompt(self,category,num_query):
        message_set=[
          {"role":"systyem","content":instruction}
          ]
        for intent in self.data[category][1:]:
          for entity_name in self.data[category][0]:
            prompt=f"""**Your Task:**
            Generate {num_query} new and unique query examples for the intent '{intent}' containing entity {entity_name}:{category}.
            """
            message_set.apppend({
              "role":"user",
              "content":prompt
            })
        return message_set
    
    def get_response(self,category,num_query):
      message_set=NLU_data_generator.create_prompt(category,num_query)
      response_set=[]
      for msg in message_set[1:]:
        response=client.chat.completions.create(
            model="deepseek-chat",
            messages=[
              message_set[0],msg
            ],
            stream=False
        ).choices[0].message.content

        response=re.sub(
          pattern=r"```json\n|\n```",
          repl='',
          string=response
        )
        response_set.append(response)
      self.responses[category]=response_set
