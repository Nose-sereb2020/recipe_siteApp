from django.shortcuts import render
import requests
import json

def request(request):
    headers_dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    api_key = 1044473351726139211
    r = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={}&categoryId=10&elements=recipeTitle,foodImageUrl,rank'.format(api_key), headers=headers_dic)
    data = r.json()
    data = json.dumps(data['result'], ensure_ascii=False)
    data = json.loads(data)
    return render(request, 'recipe_site/request.html', {'data': data})
