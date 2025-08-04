from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"📨 קיבלנו Webhook: {data}")
    return jsonify({'status': 'ok'})

app.run(host='0.0.0.0', port=8080)
