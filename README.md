# Proposed Ideas

## Idea 1: Template & Retrieval-Based Campus Life Assistant

Create a chatbot that can get user's need and retrieve from its backup dataset to recommend place to go in/around the campus. It can also analyze user's sentiment and adjust its output accordingly.

- **Customized** Backup Dataset
	- Use **structured data formats** like AIML or JSON
	- Include features, labels, and information about places to study/relax in the campus
	- Example:
```json
{

    "Nasi Kandar":{

        "type":"resturant",

        "Location":"Bell",// Can switch to coordinates in the future

        "time":"24h",// May switch to Python's datetime library

        "recommend":["Teh O Lemon Ais","Indomee Ayam"],

        "price":"medium"

    },

    "Library":{

        "type":"study area",

        "location":"A3",

        "time":{

            "Monday to Friday":"9am-10pm",

            "Weekend and Public Holidays":"9am-5pm"

        },
	"Bo Ya Xuan Chinese Restaurant":{

		"type":"restaurant",

		"location":"XMUM IAEC",

		"time":"11am-2pm, 5pm-9pm",

		"recommend":["Twice-cooked Pork Slices with Rice"],

		"price":"high"
		
	}

    }

}
```
Raw dataset will then be converted to **keyword lists**:
Sample:
```python
Bo_Ya_Xuan=["restaurant","Chinese","high-level","XMUM IAEC","11am-2pm"]
# We can then apply word embedding to facilitate retrieval afterwards
```
 

- Retrieval-Based Chatbot (May also include some templates)
	1. Take and process user's input
		1. Use VADER to analyze user's sentiment
		2. Conver text to vector
		3. May use other NLP methods like tokenization, lemmatization, etc.
	2. Retrieval Relevant Places in Our Backup Dataset
		1. May apply algorithms like cosine-similarity, SVM, ect.
		2. Find the place that best matches user's need.
	3. Construct Output
		1. Base on VADER scores of input text to decide sentiment of output (positive/negative/netural, corresponding to output templates of certain sentiment)
		2. Construct an output based on template
			1. Respond to user's sentiment
			2. Include information of the place to go to
- Expected Outcome
	- Sample:

		You: I have done well in the midterm exam and want to have a good meal.

		Chatbot: Glad to hear that! (***sentiment analysis***) For the place to go, I recommend Bo Ya Xuan Chinese Restaurant. (***recommend place to go***)
		It's located at XMUM IAEC (***location***). I strongly recommend Twice-cooked Pork Slices with Rice (***recommendation***) for you to try. However, please notice that the price would be high (***price information***).

		Supporting Data:
		- ![[Pasted image 20250515133547.png]]
- Concerns about this proposal
	- Can we include both retrieval and template?
	- ![[Pasted image 20250515134825.png]]