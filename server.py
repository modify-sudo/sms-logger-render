from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "SMS logger running"

@app.route("/sms", methods=["POST"])
def sms():
    data = request.form.to_dict()
    print("Received SMS:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
