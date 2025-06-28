# XMUM Campus Assistant

This document includes guideline of how to start the intelligent system and file structure of this project.

## How to Start the Intelligent System

Before you start the system, please make sure your system meets the following enviroment requirements:
- `Python` Environment: `v3.12.6` with `pip v25.1.1`. You may refer to this [link](https://www.python.org/downloads/) for the latest release.
- `JavaScript` Environment: `Node.js v20.18.0` with `npm v10.8.2`. You may refer to this [link](https://nodejs.org/en/download/current) for the latest release.

We created a script that enables one-click project setup: `XMUM_Campus_Assistant.bat`. You can just **double click the script to start the system**. Here is a demonstration of each step:

1. Once you click the script, a command-line window will pop up:
![](./README_figures/Pasted%20image%2020250628230110.png)
2. The command line will use `pip` and`npm` to install the required packages for backend and frontend, respectively.
![](./README_figures/Pasted%20image%2020250628230319.png)
3. After that, two new command-line window for the backend and frontend will pop up.
![](./README_figures/Pasted%20image%2020250628230428.png)
![](./README_figures/Pasted%20image%2020250628230449.png)
4. In the end, the first command-line process will open the link of the frontend [http://localhost:5173](http://localhost:5173) using the default browser of your systemautometically. If this does not work, kindly open the link manually.
5. After that, you can close the initial poped window.
![](./README_figures/Pasted%20image%2020250628230712.png)
But **do not close** the command-line window of the frontend and backend, since doing so will kill the process.
6. You can chat with the campus assistant in this page. 
![](./README_figures/Pasted%20image%2020250628230918.png)
7. The output of NLU interpreter and the infomation retrieved by the response generator will be displayed on the backend command-line window.



## Project Structure

### Backend (`py_code`)

The backend is responsible for processing user input, understanding the intent and entities, and generating an appropriate response. It is built with Flask and uses custom machine learning models for NLU.

-   `app.py`: The main Flask application that serves the chatbot API. It handles requests from the frontend, passes them to the interpreter, and returns the generated response.
-   `interpreter.py`: Contains the core Natural Language Understanding (NLU) logic. It takes raw user input and uses the trained models to identify the user's intent and extract relevant entities.
-   `response_generator.py`: Generates a text response based on the output from the NLU (`interpreter.py`).
-   `templates.py`: Defines templates for the various responses the chatbot can provide.
-   `*.ipynb` notebooks: These Jupyter notebooks (`data_generator.ipynb`, `entity_recognition.ipynb`, `intent_classification.ipynb`, `interpreter.ipynb`, `response_generator.ipynb`) were used for the development, training, and testing of the different backend components.
-   `data/`: This directory contains all data used in the project.
    -   `original_docs/`: The original source documents (e.g., markdown files) from which information was extracted.
    -   `extracted_json/`: JSON files containing structured data extracted from the `original_docs`.
        -   `database.json`: The final knowledge base of the campus assistant. It is a JSON file that contains the information of the campus.
    -   `train_data/`: Contains the datasets used to train the intent classification and entity recognition models.
    -   `trained_model/`: Stores the pre-trained machine learning models.
        -   `intent_classifier.joblib`: The saved model for intent classification.
        -   `entity_recognizer/`: The saved `spaCy` model for named entity recognition.
-   `log/`: Contains logs and reports, such as the `intent_report.md`.

### Frontend (`frontend`)

The frontend provides the user interface for interacting with the chatbot. It is a single-page application built with React and Vite, styled with Tailwind CSS.

-   `index.html`: The main entry point HTML file for the application.
-   `package.json`: Lists the project's dependencies and defines scripts for running and building the application.
-   `tailwind.config.js`: onfiguration file for the Tailwind CSS framework.
-   `src/`: Contains the main source code for the React application.
    -   `main.jsx`: The entry point of the React application, where the root component is rendered.
    -   `routes/`: Defines the application's routing structure.
        -   `App.jsx`: The main application component that sets up the page routes.
        -   `index.css`: Global styles for the application.
    -   `pages/`: Components that represent the different pages of the application.
        -   `Home.jsx`: The component for the application's home page.
        -   `CampusAssistant.jsx`: The primary component for the chat interface.
    -   `components/`: Reusable UI components used throughout the application.
        -   `ChatBubble.jsx`: A component to display a single chat message.
        -   `Logo.jsx`: A component to display the application's logo.
    -   `assets/`: Contains static assets like images.
-   `public/`: Contains static files that are served directly, such as icons and the `manifest.json`.
