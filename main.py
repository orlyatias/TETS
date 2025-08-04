from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📥 Webhook received:", data)
    return jsonify({"status": "ok"}), 200

# 🟢 חובה: לקרוא את הפורט מ־Environment משתנה
port = int(os.environ.get("PORT", 10000))
app.run(host='0.0.0.0', port=port)
