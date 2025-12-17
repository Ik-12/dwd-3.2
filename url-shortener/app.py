from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# In-memory store: short_code -> original_url
url_store = {}

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Minimal URL Shortener",
        "endpoints": {
            "POST /shorten": {"url": "https://example.com"},
            "GET /<code>": "Redirect to original URL"
        }
    })

@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    original_url = data["url"]

    code = generate_code()
    url_store[code] = original_url

    return jsonify({
        "short_code": code,
        "short_url": request.host_url + code
    })

@app.route("/<code>", methods=["GET"])
def redirect_to_url(code):
    original_url = url_store.get(code)
    if not original_url:
        return jsonify({"error": "Short code not found"}), 404

    return redirect(original_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

