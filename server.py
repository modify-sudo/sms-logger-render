from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "SMS logger running"

@app.route("/sms", methods=["POST"])
def sms():
    # httpSMS / SMS Forwarder apps usually send form-data or JSON
    data = request.form.to_dict() or (request.json or {})
    print("Received SMS:", data)

    return jsonify({"status": "ok"}), 200
