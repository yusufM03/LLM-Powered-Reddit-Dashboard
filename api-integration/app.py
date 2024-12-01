from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="your_groq_api_key")

def summarize(description):
  completion = client.chat.completions.create(
      model="llama3-70b-8192",
      messages=[
          {"role": "system", "content": "Summarize the given article."},
          {"role": "user", "content": description}
      ]
  )
  return completion['choices'][0].message.content

@app.route('/summarize', methods=['GET'])
def api_summarize():
  title = request.args.get('title')
  if not title:
      return jsonify({"error": "No title provided"}), 400
  article_content = f"Fetched content for '{title}'"  # Replace with actual fetching logic
  result = summarize(article_content)
  return jsonify({"summary": result}), 200

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
