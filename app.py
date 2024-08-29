from flask import Flask, request, jsonify
import requests
from flask import send_from_directory


app = Flask(__name__)

NGRAMS_API = "https://api.ngrams.dev"

def search_ngrams(corpus, query):
    url = f"{NGRAMS_API}/{corpus}/search"
    parameters = {'query': query, 'limit': 10}
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    corpus = request.args.get('corpus')
    query = request.args.get('query')
    if not corpus or not query:
        return jsonify({'error': 'Missing parameters'}), 400

    result = search_ngrams(corpus, query)
    if not result or not result.get('ngrams'):
        return jsonify({'error': 'No results found'}), 404

    ngram_data = [
        {
            'tokens': " ".join(token['text'] for token in ngram['tokens']),
            'absTotalMatchCount': ngram['absTotalMatchCount'],
            'relTotalMatchCount': ngram['relTotalMatchCount']
        }
        for ngram in result['ngrams']
    ]
    
    return jsonify({
        'queryTokens': result['queryTokens'],
        'ngrams': ngram_data
    })

if __name__ == '__main__':
    app.run(debug=True)
