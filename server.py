from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "Adrian Aguinaga"

@app.get("/hello")
def hello():
    message = {"message":"Hello there!"}
    return json.dumps(message)

# create an endpoint that says hello using a variable instead of using an string

app.run(debug=True)# that when i save the code, the changes are applied in to the server