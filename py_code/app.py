from interpreter import Interpreter
from response_generator import ResponseGenerator
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import spacy
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

# Initialize interpreter and response generator
interpreter = Interpreter()
response_generator = ResponseGenerator()

@app.route("/chatbot/ask", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('question', '')
        
        if not user_input:
            return jsonify({"answer": "Please enter your question."}), 400
        
        # Use interpreter to process user input
        nlu_output = interpreter.interpret(user_input)
        
        # Generate response
        #e debug
        # response = f"Intent: {nlu_output[0]['intent']}  Entities: {nlu_output[0]['entities']}   Sentiment: {nlu_output[0]['sentiment']}"
        response = response_generator.generate_response(nlu_output[0])
        print(response)
        
        return jsonify({"answer": response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"answer": "Sorry, I don't know the answer to this question."}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)