from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load summarizer model once when the server starts
summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    summary = summarizer(text, max_length=60, min_length=25, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
