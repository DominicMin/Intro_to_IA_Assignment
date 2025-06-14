# Campus Chatbot NLU Engine

This repository contains the core Natural Language Understanding (NLU) engine for a campus chatbot. The engine is responsible for processing user queries to identify intents and extract key entities. This is achieved through a combination of custom-trained machine learning models.

The project is structured around a series of Jupyter Notebooks, each handling a specific part of the NLU pipeline, from data generation to model training.

## 🚀 Core Components

The NLU engine is composed of three main parts:

1.  **Data Generation**: Utilizes Large Language Models (LLMs) like DeepSeek or Llama3 to synthetically generate training data for both intents and entities.
2.  **Intent Classification**: A machine learning model trained to understand the user's goal (e.g., asking for location, business hours, etc.).
3.  **Entity Recognition**: A Named Entity Recognition (NER) model built with spaCy to identify and extract important information from the query (e.g., "KK convenience store", "tomorrow morning").

## 📂 Repository Structure

```
.
├── .gitignore
├── py_code
│   ├── data
│   │   ├── IE
│   │   │   └── IE_lib.json
│   │   ├── extracted_json
│   │   │   ├── location.json
│   │   │   └── time.json
│   │   ├── train_data
│   │   │   ├── entity_train_data.csv
│   │   │   ├── entity_train_data.json
│   │   │   └── spacy_entity_train_data.csv
│   │   └── trained_model
│   │       ├── entity_recognizer
│   │       └── intent_classifier.joblib
│   ├── data_generator.ipynb
│   ├── entity_recognition.ipynb
│   |── intent_classification.ipynb
|   |—— interpreter.ipynb
└── README.md
```

## 📝 File Descriptions

### Python Code (`py_code/`)

-   [`py_code/data_generator.ipynb`](./py_code/data_generator.ipynb): This notebook is responsible for generating the training data. It uses LLMs with carefully crafted prompts to create varied and realistic query examples for different intents and entities.

-   [`py_code/intent_classification.ipynb`](./py_code/intent_classification.ipynb): This notebook covers the process of training the intent classifier. It loads the generated data, preprocesses it, and trains a classification model (e.g., Logistic Regression with TF-IDF features) to recognize the user's intent. The final model is saved for later use.

-   [`py_code/entity_recognition.ipynb`](./py_code/entity_recognition.ipynb): This notebook focuses on building the Named Entity Recognition (NER) model. It uses the spaCy library to train a model that can extract custom entities like `business_name`, `restaurant_name`, `facility_name`, etc., from the user's query.

### Data (`py_code/data/`)

-   `py_code/data/IE/IE_lib.json`: Contains the library of intents and entities that form the basis for data generation.

-   `py_code/data/train_data/`: This directory stores the generated training data in various formats (`.json`, `.csv`) for both intent and entity models.

-   `py_code/data/trained_model/`: This directory holds the final, trained models.
    -   `intent_classifier.joblib`: The saved intent classification pipeline.
    -   `entity_recognizer/`: The saved spaCy model for entity recognition.

## 💡 How It Works

1.  **Data Generation**: The process starts with `data_generator.ipynb`. Based on a predefined set of intents and entities in `IE_lib.json`, it prompts an LLM to generate a rich dataset of sample queries.
2.  **Model Training**:
    -   The intent data is used in `intent_classification.ipynb` to train a pipeline that can predict the intent of a given query.
    -   The entity data is used in `entity_recognition.ipynb` to train a spaCy NER model to extract relevant information.
3.  **Inference**: (Previously in `interpreter.ipynb`) The trained models are loaded to process new user queries. For a given query, the engine predicts the intent and extracts all relevant entities, providing a structured output that a chatbot can act upon.
