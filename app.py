from flask import Flask,render_template,request,jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/predict")
def predict():
    user_text = request.get_json().get("message")
    #TODO : check if user input is valid
    response = get_response(user_text)
    bot_response  = {"answer" : response}
    return jsonify(bot_response)


if __name__ == "__main__":
    app.run(debug=True)