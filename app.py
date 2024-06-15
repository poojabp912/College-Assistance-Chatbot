import sqlite3
from flask import Flask, render_template,request,jsonify

from chat import get_response,get_options

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    with sqlite3.connect('chatbot_data.db') as conn:
        cursor = conn.cursor()
        # cursor.execute('''Drop Table questions''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AutoIncrement,question TEXT)''')
        text = request.get_json().get("message")
        response = get_response(text)
        message = {"answer":response}
        if(response =="I am sorry currently I don't have information about the same"):
           cursor.execute('INSERT INTO questions (question) VALUES (?)',(text,))
        return jsonify(message)
    
@app.post("/predicts")
def predicts():
        text = request.get_json().get("message")
        options = get_options(text)
        message = {'option':options}
        return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)