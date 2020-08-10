import requests
import json

api_key = 1044473351726139211
r = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={}&categoryId=10&elements=recipeTitle,foodImageUrl,rank'.format(api_key))
data = r.json()
#print(json.dumps(data, indent=4))
data = json.dumps(data['result'], indent=2, ensure_ascii=False)
print(json.loads(data))