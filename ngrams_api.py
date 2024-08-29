import requests
import matplotlib.pyplot as plt

NGRAMS_API = "https://api.ngrams.dev"

# Corpus = language (e.g., "eng", "ger", "rus")
# Query = ngram search query (e.g., "hello"; refer to powerfulqueries.txt for specified information)
def search_ngrams(corpus, query):
    url = f"{NGRAMS_API}/{corpus}/search"

    parameters = {
        'query': query,
        'limit': 10 
    }

    return fetch_data(url, parameters)

# Fetch data from the API and handle errors
def fetch_data(url, params):
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error code: {response.status_code}")
        return None

# Print
def print_results(result):
    if result:
        print(f"Query: {result['queryTokens']}")
        print("\nNgrams:")
        for ngram in result['ngrams']:
            tokens = " ".join(token['text'] for token in ngram['tokens'])
            print(f" - Ngram: {tokens}, Absolute Matches: {ngram['absTotalMatchCount']}, Relative Matches: {ngram['relTotalMatchCount']:.10f}")
            percent = f"{ngram['relTotalMatchCount'] * 100}%"
            print(percent)

    #     ngram_data = []
    #     for ngram in result['ngrams']:
    #         relative_count = ngram['relTotalMatchCount']
    #         ngram_data.append(relative_count)
    #     return ngram_data
    
    # return []


# Main function
if __name__ == "__main__":
    # corpus = input("Please specify corpus (eng, ger, rus): ")

    # queries = []
    # for i in range(3):
    #     query = input("Please enter a query: ")
    #     queries.append(query)

    # all_data = []
    
    # for query in queries:
    #     result = search_ngrams(corpus, query)
        
    #     if result and result['ngrams']:
    #         ngram_data = print_results(result)
    #         all_data.append((query, ngram_data))
    #     else:
    #         print(f"No results found for '{query}'. Your word is very rare!")

    # labels = [query for query, _ in all_data]
    # values = [sum(data) for _, data in all_data] 

    # # bar graph
    # plt.figure(figsize=(10, 5))
    # plt.bar(labels, values, color='skyblue')
    # plt.title('Relative Match Counts of Ngrams')
    # plt.xlabel('Ngram Queries')
    # plt.ylabel('Relative Match Count')
    # plt.xticks(rotation=45)
    # plt.tight_layout()

    # # pie chart
    # plt.figure(figsize=(8, 8))
    # plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    # plt.title('Relative Match Count Distribution')
    # plt.axis('equal') 

    # # line graph
    # plt.figure(figsize=(10, 5))
    # for i, (query, ngram_data) in enumerate(all_data):
    #     plt.plot(ngram_data, marker='o', label=query)
    
    # plt.title('Line Graph of Ngram Relative Matches')
    # plt.xlabel('Match Instances (up to 10)')
    # plt.ylabel('Relative Match Count')
    # plt.xticks(range(len(all_data[0][1])), range(1, len(all_data[0][1]) + 1))
    # plt.legend(title='Queries')
    # plt.tight_layout()

    # plt.show()

    corpus = input("Please specify corpus (eng, ger, rus): ")
    query = input("Pease enter a query: ")

    result = search_ngrams(corpus, query)
    
    if result['ngrams'] == []:
        print("No results found.")
    else:
        print_results(result)

