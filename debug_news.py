# The issue was that their were no headlines for India.

import requests

newsapi = "***"
response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

print(f"Response Status Code: {response.status_code}")
print(response.text)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])

    print("Top Headlines:")
    for idx, article in enumerate(articles[:5], 1):
        print(f"{idx}. {article.get('title')}")
else:
    print("Failed to fetch news.")
    
